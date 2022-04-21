import json
from urllib import response

from  client_lib.topics import OSM_NBI_Client_admin as admin 
from  client_lib.topics import OSM_NBI_Client_nsd as nsd 
from  client_lib.topics import OSM_NBI_Client_lcm as lcm 


class Configuration:
    
    def __init__(self,conf):
        self.host = conf["host"]
        # Username for HTTP basic authentication
        self.username = conf["username"]
        # Password for HTTP basic authentication
        self.password = conf["password"]
        #Version
        self.version=conf["version"]
        #authorization token
        self.token=None
        self.admin=None





class Client:
    def __init__(self,confFile):
        self.conf=self.__readConf__(confFile) 
        self.admin=admin.Admin(self.conf)
        self.nsd=nsd.NSD(self.conf)
        self.lcm=lcm.LCM(self.conf)

    
    def __readConf__(self,confFile):
        conf_data=None
        config=None
        try:
            with open('conf.data') as json_file:
                conf_data = json.load(json_file)
        except Exception as e:
            print("Exception when trying to get conf: %s\n" % e)
        if conf_data:
            config=Configuration(conf_data)
        else:
            print("No conf")
        return config
    
    def getNSDs(self):
        response = self.nsd.getNSDs()
        ns_desc_json=json.loads(json.dumps(response))
        return ns_desc_json

    #if name is None return all ids
    def getNS_id(self,ns_name=None):
        target_ns_id=dict()
        response = self.nsd.getNSDs()
        if response:
            ns_desc_json=json.loads(json.dumps(response))
            #print(json.dumps(ns_desc_json))
            for ns_desc in ns_desc_json:
                if ns_name:
                    if ns_desc["name"]==ns_name:
                        #print("NS EXISTS")
                        #print(ns_desc["name"],ns_desc["_id"])
                        target_ns_id[ns_desc["name"]]=ns_desc["_id"]
                else:
                    target_ns_id[ns_desc["name"]]=ns_desc["_id"]


            return target_ns_id
        else:
            return False


    def get_token_id(self):
       resp=self.admin.requestNewToken()
       if resp:
           return(resp["id"])
       return resp


    def get_vim_account(self):
        vim_account_id=None
        response = self.admin.getVimAccounts()
        status=response[0]
        data=response[1]
        if status==200:
            vim_Accounts_json=json.loads(json.dumps(data))
            #print(json.dumps(ns_desc_json))
            for vim_account in vim_Accounts_json:
                if "_id" in vim_account:
                    #print(vim_account["_id"])
                    vim_account_id=vim_account["_id"]
            return vim_account_id
        else:
            return False