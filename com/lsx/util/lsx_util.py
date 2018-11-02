#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lsx_util.py
# @Author: Armote
# @Date  : 2018/10/30 0030
# @Desc  :Armote工具[模板]
import time
import datetime


def getNowTime():
    """来个时间戳"""
    t = time.time()
    nowTime = lambda: int(round(t * 1000))
    return str(nowTime())

