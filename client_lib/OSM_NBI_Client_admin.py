from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 


class Admin:
    def __init__(self,configuration ):
        self.configuration = configuration
        self.headers=None
        self.main_topic=None
        self.topic=None
        self.payload=None
        self.ApiReq=None

    
    def requestNewToken(self):
        #TODO: check forconnectivity
        gen_api=api_help.GenericApi("admin","tokens","POST",{
        'Content-Type': 'application/json'
        })
        self.main_topic=gen_api.main_topic
        self.headers= gen_api.headers
        self.topic=gen_api.topic
        self.action=gen_api.action  
        self.ApiReq= api_help.ApiRequest(self.configuration,self.headers)

        if self.headers is None:
            print("Ooops")
            return None
        pprint("Request New Token")
        self.payload="{\"username\": \""+ self.configuration.username+"\",  \"password\": \""+self.configuration.password+"\"}"
        return (self.ApiReq.send_request("POST",self.main_topic,self.topic,self.payload) )


