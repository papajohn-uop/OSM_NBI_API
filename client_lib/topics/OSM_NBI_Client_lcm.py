from curses import reset_prog_mode
from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 


class LCM:
    def __init__(self,configuration):
        self.configuration = configuration
        self.generic_api=None


    def __ns_instances__(self,payload):
        gen_api=api_help.GenericApi("nslcm","ns_instances","POST",{
                                'Authorization': 'Bearer ' + self.configuration.token 
                                })
        self.generic_api=gen_api
        self.payload=None
        self.ApiReq= api_help.ApiRequest(self.configuration,self.generic_api.headers)
        if self.generic_api.headers is None:
            print("Ooops")
            return None
        if self.configuration.token is None:
            print("No authorzation")
            return None
        pprint("LCM-CREATE NS INSTANCE")
        self.payload=payload

        # {
        # "nsName": "my_NS_NAME",
        # "nsdId": "f2d461f6-70f2-4b30-b820-863dfcfbc281",
        # "vimAccountId": "2256c8dd-e3a5-4082-b984-b7f87540680a"
        # }

       
        # return
 
        resp= self.ApiReq.send_request(self.generic_api.action,self.generic_api.main_topic,self.generic_api.topic,json.dumps(self.payload))
        print(resp)
        # print(resp["status"])
        
        if  "id" not in resp: 
            print("Command failed")
            print(resp.status)
            return False
        
        return resp

    def ns_instances(self,nsName,nsdID,vimAccountId):
        try:
            #payload
            payload=dict()
            payload["nsName"]=nsName
            payload["nsdId"]=nsdID
            payload["vimAccountId"]=vimAccountId
            response = self.__ns_instances__(payload)
        except Exception as e:
            print("Exception when calling LCM->ns_instances: %s\n" % e)
            return None


        return response["id"]


