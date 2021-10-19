from pprint import pprint
import http.client
import json
import yaml


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

        try:
            resp_yaml=yaml.safe_load(data)

            return resp_yaml
        except yaml.YAMLError as exc:
            print(exc)
            return None


