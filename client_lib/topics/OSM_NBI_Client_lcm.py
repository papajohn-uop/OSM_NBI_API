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
        # self.main_topic=None
        # self.headers= None
        # self.topic=None
        # self.action=None
        # self.payload=None
        # self.ApiReq= None


    def __createNS_Instance__(self):
        gen_api=api_help.GenericApi("nslcm","ns_instances","POST",{
                                'Authorization': 'Bearer ' + self.configuration.token 
                                })
        self.generic_api=gen_api
        # self.main_topic=gen_api.main_topic
        # self.headers= gen_api.headers
        # self.topic=gen_api.topic
        # self.action=gen_api.action  
        self.payload=None
        self.ApiReq= api_help.ApiRequest(self.configuration,self.generic_api.headers)
        if self.generic_api.headers is None:
            print("Ooops")
            return None
        if self.configuration.token is None:
            print("No authorzation")
            return None
        pprint("LCM-CREATE NS INSTANCE")
        self.payload=dict()

        # {
        # "nsName": "my_NS_NAME",
        # "nsdId": "f2d461f6-70f2-4b30-b820-863dfcfbc281",
        # "vimAccountId": "2256c8dd-e3a5-4082-b984-b7f87540680a"
        # }

       
        # return
        resp= self.ApiReq.send_request(self.generic_api.action,self.generic_api.main_topic,self.generic_api.topic,self.payload)
        # print(resp)
        # print(resp["status"])
        if resp["status"]!=200: 
            print("Command failed")
            # return False
        return resp

    def getNSDs(self):
        try:
            # Get NSDs
            response = self.__getNSDs__()
        except Exception as e:
            print("Exception when calling NSD->getNSDs: %s\n" % e)
            return None


        return response


