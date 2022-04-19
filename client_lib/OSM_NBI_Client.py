import json

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

    def getNS_id(self,ns_name):
        target_ns_id=None
        response = self.nsd.getNSDs()
        ns_desc_json=json.loads(json.dumps(response))
        #print(json.dumps(ns_desc_json))
        for ns_desc in ns_desc_json:
            if ns_desc["name"]==ns_name:
                print("NS EXISTS")
                print(ns_desc["name"],ns_desc["_id"])
                target_ns_id=ns_desc["_id"]
        return target_ns_id


    def get_token(self):
       resp=self.admin.requestNewToken()
       return resp
