from __future__ import print_function

import os
import sys
import requests
import json
import time
import re
import copy
import logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
#from tests.fake import fake, fake_post
#FAKE=True
FAKE=False

class DeploymentTimeoutError(Exception):
    pass

class DeploymentError(Exception):
    pass


from dnac import get_auth_token, create_url, wait_on_task

def get_url(url, extraHeaders={}):

    url = create_url(path=url)
    print(url)
    token = get_auth_token()
    headers = copy.deepcopy(extraHeaders)
    headers.update({'X-auth-token' : token['token'], "__runsync": "true"})

    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    return response.json()

def post_sync(url, data):

    token = get_auth_token()
    url = create_url(path=url)
    headers= { 'x-auth-token': token['token'], 'content-type' : 'application/json', '__runsync' :'true'}
    logging.debug(headers)
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except requests.exceptions.RequestException  as cerror:
        print ("Error processing request", cerror)
        sys.exit(1)

    return response.json()

def post_and_wait(url, data):

    token = get_auth_token()
    url = create_url(path=url)
    headers= { 'x-auth-token': token['token'], 'content-type' : 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    except requests.exceptions.RequestException  as cerror:
        print ("Error processing request", cerror)
        sys.exit(1)

    taskid = response.json()['response']['taskId']
    print ("Waiting for Task %s" % taskid)
    task_result = wait_on_task(taskid, token)

    return task_result

def delete(url):

    token = get_auth_token()
    url = create_url(path=url)
    headers= { 'x-auth-token': token['token'], 'content-type' : 'application/json'}

    try:
        response = requests.delete(url, headers=headers, verify=False)
    except requests.exceptions.RequestException  as cerror:
        print ("Error processing request", cerror)
        sys.exit(1)

    if 'errorCode' in response.json()['response']:
        return response.json()['response']
    taskid = response.json()['response']['taskId']
    #print("Waiting for Task %s" % taskid)
    task_result = wait_on_task(taskid, token, timeout=10, retry_interval=2)

    return task_result