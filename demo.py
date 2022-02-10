from pprint import pprint
import http.client
import json
import yaml

import client_lib.OSM_NBI_Client as OSM_NBI_Client

import client_lib.OSM_NBI_Client_admin as OSM_NBI_Client_admin
import client_lib.OSM_NBI_Client_nsd as OSM_NBI_Client_nsd




def OSM_TEST():

    conf_data=None
    try:
        with open('conf.data') as json_file:
            conf_data = json.load(json_file)
    except Exception as e:
        print("Exception when trying to get conf: %s\n" % e)
    if conf_data:
        config=OSM_NBI_Client.Configuration(conf_data)
    else:
        print("No conf")
        return


    if (get_token(config)):
        try:
            # Get NSDs

            NBI_nsd_client =OSM_NBI_Client_nsd.NSD(config)

            response = NBI_nsd_client.getNSDs()
        
            for resp in response:
                pprint(resp["name"])
        except Exception as e:
            print("Exception when calling NSD->getNSDs: %s\n" % e)
    else:
        print("FAIL.......")





def get_token(config):
   

    NBI_admin_client =OSM_NBI_Client_admin.Admin(config)


    try:
        # Request a new Token
        response = NBI_admin_client.requestNewToken()
        config.token=response["id"]
    except Exception as e:
        print("Exception when calling Admin->requestNewToken: %s\n" % e)
        return False
    return True


OSM_TEST()

