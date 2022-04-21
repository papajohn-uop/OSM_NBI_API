from pprint import pprint
import http.client
import json
import yaml


from  client_lib import api_helper as api_help 

class Admin:
    def __init__(self,configuration ):
        self.configuration = configuration
        self.ApiReq=None
        #New approach use genericapi
        self.genericApi=None

    
    def __requestNewToken__(self):
        #TODO: check forconnectivity
        gen_api=api_help.GenericApi("admin","tokens","POST",{
        'Content-Type': 'application/json'
        })
        self.genericApi=gen_api
        self.ApiReq= api_help.ApiRequest(self.configuration,self.genericApi.headers)
        if self.genericApi.headers is None:
            print("Ooops")
            return None
        # pprint("Request New Token")
        self.payload="{\"username\": \""+ self.configuration.username+"\",  \"password\": \""+self.configuration.password+"\"}"
        return (self.ApiReq.send_request(self.genericApi.action,self.genericApi.main_topic,self.genericApi.topic,self.payload) )

    def requestNewToken(self):
        status=None
        data=None
        try:
        # Request a new Token
            response = self.__requestNewToken__()
            status=response[0]
            data=response[1]
            if status==200:
                self.configuration.token=data["id"]
            else:
                return False
        except Exception as e:
            print("Exception when calling Admin->requestNewToken: %s\n" % e)
            return False
        return data
        return(self.__requestNewToken__())



    def __get_VIM_accounts__(self):
        #TODO: check forconnectivity
        gen_api=api_help.GenericApi("admin","vim_accounts","GET",{
                                'Authorization': 'Bearer ' + self.configuration.token 
                                })
        self.genericApi=gen_api
        # self.main_topic=gen_api.main_topic
        # self.headers= gen_api.headers
        # self.topic=gen_api.topic
        # self.action=gen_api.action  
        self.ApiReq= api_help.ApiRequest(self.configuration,self.genericApi.headers)
        if self.genericApi.headers is None:
            print("Ooops")
            return None
        #pprint("Get vim_accounts")
        # self.payload="{\"username\": \""+ self.configuration.username+"\",  \"password\": \""+self.configuration.password+"\"}"
        return (self.ApiReq.send_request(self.genericApi.action,self.genericApi.main_topic,self.genericApi.topic,self.genericApi.payload) )





    def getVimAccounts(self):
        try:
        # GEt vim accounts list
            response = self.__get_VIM_accounts__()
            status=response[0]
            data=response[1]
            if status==200:
                return response
           # self.configuration.token=response["id"]
        except Exception as e:
            print("Exception when calling Admin->requestNewToken: %s\n" % e)
            return False
        return True
