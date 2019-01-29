# Cisco DNA Center Site tool.

a simple tool to get/add/delete Cisco DNA Center sites

## get sites
```buildoutcfg
$ ./site.py 
https://sandboxdnac2.cisco.com:8080/api/v1/group/count?groupType=SITE
COUNT:11
https://sandboxdnac2.cisco.com:8080/api/v1/group?groupType=SITE&offset=1&limit=500
name|type|address|id
Global/AUS|area|None|f874200e-8a1e-46e9-8f42-808246232544
Global/EU|area|None|132f5134-b3fc-4757-aa78-8f4de2f8d8f4
Global/AUS/Sydney/SYD1|building|177 Pacific Highway, North Sydney New South Wales 2060, Australia|ba06348e-ee80-4058-bb23-f0c9a5fd728b
Global/AUS/Sydney|area|None|d548ad53-09e5-4369-bd20-836aa85fd7b1
Global/EU/Barcelona|building|Carrer De Willy Brandt, 08191 Rubí, Barcelona, Spain|40170253-368a-4b49-8d7e-8df993c6cf50
Global/USA|area|None|267d75a9-39b5-497d-b2f5-15fa5b2eb7a4
Global/AUS/Sydney/SYD1/floor23|floor|177 Pacific Highway, North Sydney New South Wales 2060, Australia|38296369-aa23-4e40-87b2-a69d3fcc92e8
Global/AUS/Sydney/SYD1/floor22|floor|177 Pacific Highway, North Sydney New South Wales 2060, Australia|c1f1c6e9-e78a-474c-b4a0-26df08b49482
Global/AUS/Sydney/STL-1|building|201 Pacific Highway, St Leonards New South Wales 2065, Australia|4e91d543-9d63-41b4-a4ba-6e0530859216

```

## Add sites.
Note --commit is required for api calls to be made
````buildoutcfg
$ ./site.py --add work_files/simple-del.csv --commit
https://sandboxdnac2.cisco.com:8080/api/v1/group/count?groupType=SITE
COUNT:9
https://sandboxdnac2.cisco.com:8080/api/v1/group?groupType=SITE&offset=1&limit=500
adding from work_files/simple-del.csv
Adding Global/New[area] to Global[area]:Status:Success:Site Creation completed successfully
````
## Delete site
Note --commit is required for api calls to be made
```buildoutcfg
$ ./site.py --delete work_files/simple-del.csv --commit
https://sandboxdnac2.cisco.com:8080/api/v1/group/count?groupType=SITE
COUNT:11
https://sandboxdnac2.cisco.com:8080/api/v1/group?groupType=SITE&offset=1&limit=500
deleting from None
Global/New
Deleting Global/New/First:(5a9dc015-fbcb-4bc0-9ffa-a4a22863727d)
Group is deleted successfully
Deleting Global/New:(ad82c58f-00f5-4baf-97e3-4442a8720912)
Group is deleted successfully
Finished deleting Global/New

```