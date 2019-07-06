#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from framework.read_config import ConfigRead
from framework.logger import Logger

logger = Logger(logger='MailSend').get_log()


def send_mail(filename):
    f = open(filename, 'rb')
    mail_body = f.read()
    f.close()
    config = ConfigRead()
    smtp_server = config.get_value('mailConfig', 'smtp_server')
    sender = config.get_value('mailConfig', 'sender')
    receiver = config.get_value('mailConfig', 'receiver')
    password = config.get_value('mailConfig', 'password')
    mail_title = '主题：测试报告'

    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    try:
        server = smtplib.SMTP(smtp_server,25)
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        logger.info('邮件发送成功')
        server.quit()
    except smtplib.SMTPException as e:
        logger.error('发送失败：%s' % e)
    

