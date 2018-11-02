#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : email_msg.py
# @Author: Armote
# @Date  : 2018/10/30 0030
# @Desc  :

import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "zjt75225@163.com"  # 用户名
mail_pass = "jd13517117466"  # SMTP授权码(不是密码)

content = '测试完啦,感谢!'
sender = 'zjt75225@163.com' #发件人
receiver = '413066165@qq.com,2632127500@qq.com'# 收件人后面用逗号隔开添加
cc = '1157715071@qq.com,564073104@qq.com'# 抄送邮件 后面用逗号隔开添加

message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = sender
message['To'] =  receiver # 接收邮件
message['Cc'] =  cc
message['Subject'] = 'Python SMTP Mail 使用程序发送邮件测试' # 邮件标题

#添加附件
att = MIMEText(open(u'D:\\file\\csv\\wikiped.xlsx','rb').read(),'base64','utf-8')
att['Content-type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
attName = 'attachment; filename ="资料.xlsx"'
att['Content-Disposition'] = attName
#message.attach(att)

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(message['From'],message['To'].split(','), message.as_string())  # 发送：message对象需要From(发件人),To(收件人),Cc(抄送),Subject(邮件标题)
    print("mail has been send successfully.")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print(e)

