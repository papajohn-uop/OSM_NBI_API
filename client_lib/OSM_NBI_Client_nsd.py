from curses import reset_prog_mode
from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 


class NSD:
    def __init__(self,configuration):
        self.configuration = configuration
        self.main_topic=None
        self.headers= None
        self.topic=None
        self.action=None
        self.payload=None
        self.ApiReq= None


    def __getNSDs__(self):
        gen_api=api_help.GenericApi("nsd","ns_descriptors","GET",{
                                'Authorization': 'Bearer ' + self.configuration.token 
                                })
        self.main_topic=gen_api.main_topic
        self.headers= gen_api.headers
        self.topic=gen_api.topic
        self.action=gen_api.action  
        self.payload=None
        self.ApiReq= api_help.ApiRequest(self.configuration,self.headers)
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

    def getNSDs(self):
        try:
            # Get NSDs
            response = self.__getNSDs__()
        except Exception as e:
            print("Exception when calling NSD->getNSDs: %s\n" % e)
            return None


        return response


