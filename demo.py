from pprint import pprint
import http.client
import json
import yaml

import client_lib.OSM_NBI_Client as OSM_NBI_Client




config=OSM_NBI_Client.Configuration()
gen_API=OSM_NBI_Client.api_help.GenericApi("admin","tokens","POST",{
        'Content-Type': 'application/json'
        })
NBI_admin_client =OSM_NBI_Client.admin_client.Admin(config)


try:
    # Request a new Token
    response = NBI_admin_client.requestNewToken()
    print(response)
    print(response["id"])
    config.token=response["id"]
    print(config.token)
except Exception as e:
    print("Exception when calling Admin->requestNewToken: %s\n" % e)

try:
    # Get NSDs
    NBI_nsd_client =OSM_NBI_Client.nsd_client.NSD(config)

    response = NBI_nsd_client.getNSDs()
    # print(response)
    # print("*************")
    # print(type(response))
    # print("*************")
    # pprint(response[0])
    # print("*************")
    # pprint(response[0]["description"])
    # print("*************")
    # pprint(response[0]["id"])
    # print("*************")
    # pprint(response[0]["name"])
    pprint(len(response))
    for resp in response:
        pprint("***************")
        pprint(resp)
        pprint("***************")
        pprint(resp["description"])
except Exception as e:
    print("Exception when calling NSD->getNSDs: %s\n" % e)



