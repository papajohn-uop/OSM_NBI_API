from pprint import pprint
import http.client
import json
import yaml

from  client_lib import OSM_NBI_Client_admin as admin 



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





