from pprint import pprint
import http.client
import json
import yaml

class Configuration:
    def __init__(self):
        self.host = "xx.xx.xx.xx"
        # Username for HTTP basic authentication
        self.username = "username"
        # Password for HTTP basic authentication
        self.password = "password"
        #Version
        self.version="v1"
        #authorization token
        self.token=None

class GenericApi():
    def __init__(self,main_topic,topic,action,headers):
        self.main_topic=main_topic
        self.topic=topic
        self.action=action
        self.headers=headers
        self.payload=None



class ApiRequest():
    def __init__(self,configuration,headers):
        self.configuration=configuration
        self.conn=http.client.HTTPConnection(configuration.host)
        self.headers=headers
       
    def send_request(self,action,main_topic, topic,payload):
        self.conn.request(action, "/osm/"+main_topic+"/"+self.configuration.version+"/" + topic, payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
    #    print(data.decode("utf-8"))
#        responseObject = json.loads(data)
        try:
            resp_yaml=yaml.safe_load(data)
           # print(resp_yaml)
            return resp_yaml
        except yaml.YAMLError as exc:
            print(exc)
            return None
     #   print(data.decode())
        #return data.decode("utf-8")


class Admin:
    def __init__(self,configuration, gen_api:GenericApi):
        self.configuration = configuration
        self.main_topic=gen_api.main_topic
        self.headers= gen_api.headers
        self.topic=gen_api.topic
        self.action=gen_api.action  
        self.payload=None
        self.ApiReq= ApiRequest(configuration,self.headers)

    
    def requestNewToken(self):
        #TODO
        if self.headers is None:
            print("Ooops")
            return None
        pprint("Request New Token")
        self.payload="{\"username\": \""+ self.configuration.username+"\",  \"password\": \""+self.configuration.password+"\"}"
        return (self.ApiReq.send_request("POST",self.main_topic,self.topic,self.payload) )



class NSD:
    def __init__(self,configuration, gen_api:GenericApi):
        self.configuration = configuration
        self.main_topic=gen_api.main_topic
        self.headers= gen_api.headers
        self.topic=gen_api.topic
        self.action=gen_api.action  
        self.payload=None
        self.ApiReq= ApiRequest(configuration,self.headers)


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








# config=Configuration()
# gen_API=GenericApi("admin","tokens","POST",{
#         'Content-Type': 'application/json'
#         })
# NBI_admin_client =Admin(config,gen_API)


# try:
#     # Request a new Token
#     response = NBI_admin_client.requestNewToken()
# #    print(response)
# #    print(response["id"])
#     config.token=response["id"]
#     print(config.token)
# except Exception as e:
#     print("Exception when calling Admin->requestNewToken: %s\n" % e)

# try:
#     # Get NSDs
#     gen_API=GenericApi("nsd","ns_descriptors","GET",{
#                                 'Authorization': 'Bearer ' + config.token 
#                                 })
#     NBI_nsd_client =NSD(config,gen_API)

#     response = NBI_nsd_client.getNSDs()
#     print(response)
#     print("*************")
#     pprint(response[0])
#     print("*************")
#     pprint(response[0]["description"])
#     print("*************")
#     pprint(response[0]["id"])
#     print("*************")
#     pprint(response[0]["name"])
# except Exception as e:
#     print("Exception when calling NSD->getNSDs: %s\n" % e)



# # try:
# #     # Get NSDs
# #     NBI_nsd_client =NSD(config)

# #     response = NBI_nsd_client.getNSDs()
# #     print(response)
# #     print("*************")
# #     pprint(response[0])
# #     print("*************")
# #     pprint(response[0]["description"])
# #     print("*************")
# #     pprint(response[0]["id"])
# #     print("*************")
# #     pprint(response[0]["name"])
# # except Exception as e:
# #     print("Exception when calling NSD->getNSDs: %s\n" % e)