from pprint import pprint
import http.client
import json
import yaml

import client_lib.OSM_NBI_Client as OSM_NBI_Client




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
            gen_API=OSM_NBI_Client.GenericApi("nsd","ns_descriptors","GET",{
                                        'Authorization': 'Bearer ' + config.token 
                                        })
            NBI_nsd_client =OSM_NBI_Client.NSD(config,gen_API)

            response = NBI_nsd_client.getNSDs()
        
            for resp in response:
                pprint(resp["name"])
        except Exception as e:
            print("Exception when calling NSD->getNSDs: %s\n" % e)
    else:
        print("FAIL.......")





def get_token(config):
   
    gen_API=OSM_NBI_Client.GenericApi("admin","tokens","POST",{
        'Content-Type': 'application/json'
        })
    NBI_admin_client =OSM_NBI_Client.Admin(config,gen_API)


    try:
        # Request a new Token
        response = NBI_admin_client.requestNewToken()
        config.token=response["id"]
    except Exception as e:
        print("Exception when calling Admin->requestNewToken: %s\n" % e)
        return False
    return True


OSM_TEST()

