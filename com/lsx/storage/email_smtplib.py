#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : email_smtplib.py
# @Author: Armote
# @Date  : 2018/10/30 0030
# @Desc  :使用smtp发送邮件

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello World")
msg['Subject'] = 'An Email Alert'
msg['From'] = 'zjt75225@163.com'
msg['To'] = '413066165@qq.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()