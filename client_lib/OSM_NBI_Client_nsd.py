from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 


class NSD:
    def __init__(self,configuration, gen_api:api_help.GenericApi):
        self.configuration = configuration
        self.main_topic=gen_api.main_topic
        self.headers= gen_api.headers
        self.topic=gen_api.topic
        self.action=gen_api.action  
        self.payload=None
        self.ApiReq= api_help.ApiRequest(configuration,self.headers)


    def getNSDs(self):
        if self.headers is None:
            print("Ooops")
            return None
        if self.configuration.token is None:
            print("No authorzation")
            return None
        pprint("Get NSDS")
        self.payload=""
        self.topic="ns_descriptors"

        return (self.ApiReq.send_request("GET",self.main_topic,self.topic,self.payload) )






