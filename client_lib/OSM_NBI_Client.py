from pprint import pprint
import http.client
import json
import yaml

from  client_lib import OSM_NBI_Client_admin as admin_client
from  client_lib import OSM_NBI_Client_nsd as nsd_client
from  client_lib import api_helper as api_help 

class Configuration:
    def __init__(self):
        self.host = "10.10.10.84"
        # Username for HTTP basic authentication
        self.username = "papajohn"
        # Password for HTTP basic authentication
        self.password = "P@paj0hn"
        #Version
        self.version="v1"
        #authorization token
        self.token=None

# class GenericApi():
#     def __init__(self,main_topic,topic,action,headers):
#         self.main_topic=main_topic
#         self.topic=topic
#         self.action=action
#         self.headers=headers
#         self.payload=None



# class ApiRequest():
#     def __init__(self,configuration,headers):
#         self.configuration=configuration
#         self.conn=http.client.HTTPConnection(configuration.host)
#         self.headers=headers
       
#     def send_request(self,action,main_topic, topic,payload):
#         self.conn.request(action, "/osm/"+main_topic+"/"+self.configuration.version+"/" + topic, payload, self.headers)
#         res = self.conn.getresponse()
#         data = res.read()

#         try:
#             resp_yaml=yaml.safe_load(data)

#             return resp_yaml
#         except yaml.YAMLError as exc:
#             print(exc)
#             return None




# class NSD:
#     def __init__(self,configuration, gen_api:GenericApi):
#         self.configuration = configuration
#         self.main_topic=gen_api.main_topic
#         self.headers= gen_api.headers
#         self.topic=gen_api.topic
#         self.action=gen_api.action  
#         self.payload=None
#         self.ApiReq= ApiRequest(configuration,self.headers)


#     def getNSDs(self):
#         if self.headers is None:
#             print("Ooops")
#             return None
#         if self.configuration.token is None:
#             print("No authorzation")
#             return None
#         pprint("Get NSDS")
#         self.payload=""
#         self.topic="ns_descriptors"

#         return (self.ApiReq.send_request("GET",self.main_topic,self.topic,self.payload) )






