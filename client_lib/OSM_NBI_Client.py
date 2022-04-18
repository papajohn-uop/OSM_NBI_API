import json

from  client_lib.topics import OSM_NBI_Client_admin as admin 
from  client_lib.topics import OSM_NBI_Client_nsd as nsd 


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
            
