# -*- coding: utf-8 -*-
import requests

url = 'http://www.dianping.com/beijing/ch95/g25147'

req = requests.get(url=url).text

print(req)

