from curses import reset_prog_mode
from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 


class NSD:
    def __init__(self,configuration):
        self.configuration = configuration
        self.ApiReq= None


    def __getNSDs__(self):
        gen_api=api_help.GenericApi("nsd","ns_descriptors","GET",{
                                'Authorization': 'Bearer ' + self.configuration.token 
                                })
        self.genericApi=gen_api
        self.ApiReq= api_help.ApiRequest(self.configuration,self.genericApi.headers)
        if self.genericApi.headers is None:
            print("Ooops")
            return None
        if self.configuration.token is None:
            print("No authorzation")
            return None
        # pprint("Get NSDS")
        self.payload=""
        self.topic="ns_descriptors"
        return (self.ApiReq.send_request("GET",self.genericApi.main_topic,self.genericApi.topic,self.genericApi.payload) )

    def getNSDs(self):
        ns_descs_json=None
        try:
            # Get NSDs
            response = self.__getNSDs__()
            status=response[0]
            data=response[1]
  
            if status==200:
                ns_descs_json=json.loads(json.dumps(data))
                return ns_descs_json
            else:
                return data
        except Exception as e:
            print("Exception when calling NSD->getNSDs: %s\n" % e)
            return None


        # return response


