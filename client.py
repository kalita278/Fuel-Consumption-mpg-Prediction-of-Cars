# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:47:41 2023

@author: dell1
"""
import requests
import json
url  = "http://127.0.0.1:8080/api"
data = json.dumps({'cyl':1,'disp':2,'hp':7,'wt':50,'acc':8,"yr":90,'origin_1':1,'origin_2':0,'origin_3':0})
r = requests.post(url,data)
print(r.json())