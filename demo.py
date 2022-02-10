from pprint import pprint
import http.client
import json
import yaml

import client_lib.OSM_NBI_Client as OSM_NBI_Client

import client_lib.OSM_NBI_Client_admin as OSM_NBI_Client_admin
import client_lib.OSM_NBI_Client_nsd as OSM_NBI_Client_nsd




def OSM_TEST():


    client=OSM_NBI_Client.Client("conf.data")

    if (client.admin.requestNewToken()):
        NBI_nsd_client =OSM_NBI_Client_nsd.NSD(client.conf)
        #response = NBI_nsd_client.getNSDs()
        response = client.nsd.getNSDs()
        for resp in response:
            pprint(resp["name"])



OSM_TEST()

