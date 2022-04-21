from pprint import pprint
import http.client
import json
import yaml

import client_lib.OSM_NBI_Client as OSM_NBI_Client

#import client_lib.OSM_NBI_Client_nsd as OSM_NBI_Client_nsd




def OSM_TEST():


    client=OSM_NBI_Client.Client("conf.data")

    if (client.admin.requestNewToken()):
        #NBI_nsd_client =OSM_NBI_Client_nsd.NSD(client.conf)
        #response = NBI_nsd_client.getNSDs()
        response = client.nsd.getNSDs()
        for resp in response:
            pprint(resp["name"])

  


def OSM_DEPLOY_NS(ns_name):


    client=OSM_NBI_Client.Client("conf.data")

    #Try and create a NS instance

    '''
    3 arguments required minimum (until all model is supported)
    nsName*	string: Human-readable name of the NS instance to be created.
    nsdId*	string($uuid):Identifier of the NSD that defines the NS instance to be created.
    vimAccountId*	string($uuid):Identifier of the VIM Account where the NS instance shall be created.
    
    nsName: User selected
    nsdId: The id of the NS to de created. Taken by the /nsd/v1/ns_descriptors
    '''
    target_ns_id=None
    vim_account_id=None
    if (client.admin.requestNewToken()):
        print("CREATE NS INSTANCE")   
        print("Step1: Get VIM accounts")
        response=client.admin.getVimAccounts()
        # print(json.dumps(response))
        vim_Accounts_json=json.loads(json.dumps(response))
        for vim_account in vim_Accounts_json:
            if "_id" in vim_account:
                print(vim_account["_id"])
                vim_account_id=vim_account["_id"]

        print("Step2: Get NS DESCRIPTORS ids")
        response = client.nsd.getNSDs()
        ns_desc_json=json.loads(json.dumps(response))
        #print(json.dumps(ns_desc_json))
        for ns_desc in ns_desc_json:
            if ns_desc["name"]==ns_name:
                print("NS EXISTS")
                print(ns_desc["name"],ns_desc["_id"])
                target_ns_id=ns_desc["_id"]

        if target_ns_id is None:
            print("NO SUCH NS EXISTS")
            return False

        print("Step3: Call /nslcm/v1/ns_instances endpoint")
        ns_instance_id=client.lcm.ns_instances("client_test_name",target_ns_id,vim_account_id)
        print(ns_instance_id)

       
        
    # resp=client.lcm.__createNS_Instance__()
    # print(resp)


# OSM_TEST()


#print(OSM_DEPLOY_NS("SimpleNSD"))

# #exit()
# client=OSM_NBI_Client.Client("conf.data")
# if client.admin.requestNewToken():
#     ns_id=client.getNS_id("SimpleNSD")
#     vim_account=client.get_vim_account()
#     print("-----------------------")
#     print(ns_id)
#     print(vim_account)



#Get token
print("**********************NBI******************")
print("\n\n*************GET TOKEN***************")
client=OSM_NBI_Client.Client("conf.data")
result=client.admin.requestNewToken()
print(result)

#Get NSDs
print("\n\n*************GET NSDs***************")
print("Whole GET NSDs Response (NBI API)")
client=OSM_NBI_Client.Client("conf.data")
result=client.admin.requestNewToken()
if result:
    result=client.nsd.getNSDs()
    print(result)
else:
    print("NO AUTHORIZATION")

print("\n\n\n\n**********************WRAPPERS******************")
#Get token id
print("TOKEN ID (WRAPPER)")
client=OSM_NBI_Client.Client("conf.data")
result=client.get_token_id()
print(result)


#Get NSDs IDs
print("Get ALL nsds ids")
client=OSM_NBI_Client.Client("conf.data")
result=client.admin.requestNewToken()
if result:
    result=client.getNS_id()
    if len(result)>0:
        print(result)
    else:
        print("NO NSDs")
else:
    print("NO AUTHORIZATION")

#Get NSD ID
print("Get NSD id ")
client=OSM_NBI_Client.Client("conf.data")
result=client.admin.requestNewToken()
if result:
    result=client.getNS_id("SimpleNSD")
    if len(result)>0:
        print(result)
    else:
        print("NO NSDs")
else:
    print("NO AUTHORIZATION")

#Get NSD ID
print("Get NSD id ")
client=OSM_NBI_Client.Client("conf.data")
result=client.admin.requestNewToken()
if result:
    result=client.getNS_id("SimpleNSD_FAKE")
    if len(result)>0:
        print(result)
    else:
        print("NO NSD with such name")
else:
    print("NO AUTHORIZATION")

