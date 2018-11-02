#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : requestUrl.py
# @Author: Armote
# @Date  : 2018/10/19 0019
# @Desc  :

from urllib import request
from urllib import parse
import json

url = "武汉"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


req = request.Request(url="http://www.weather.com.cn/data/sk/101200901.html", headers=headers)

print("https://www.sojson.com/open/api/weather/json.shtml?city="+parse.quote(url))
result_data = request.urlopen(req).read()
result_data = result_data.decode("utf-8")
result_data = json.loads(result_data)
print(result_data)