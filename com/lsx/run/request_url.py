#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : request_url.py
# @Author: Armote
# @Date  : 2018/10/19 0019
# @Desc  :

from urllib import request
import json

url = "https://www.sojson.com/open/api/lunar/json.shtml"
result_data = json.loads(request.urlopen(request.Request(url)).read())
print("%s%s月%s " % (result_data["data"]["cnyear"],result_data["data"]["cnmonth"],result_data["data"]["cnday"]))




#查五天t天气==================================================================
from urllib import request
from urllib import parse
import json

url = "武汉"
result_data = request.urlopen(request.Request("https://www.sojson.com/open/api/weather/json.shtml?city="+parse.quote(url))).read()
result_data = result_data.decode("utf-8")
result_data = json.loads(result_data)
for ea in result_data["data"]["forecast"]:
  print ("日期：%s\t\t高温:%s\t\t低温：%s\t\t天气：%s" % (ea["date"],ea["high"][2:],ea["low"][2:],ea["type"]))