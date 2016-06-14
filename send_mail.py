# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:08:00 2016

@author: HOME
"""

import smtplib
import base64
import time
import datetime

print str(datetime.datetime.now())


def send_mail(pwd):

    password = base64.b64decode(pwd)

    # in the prod system, ask the mail exchange server and port

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    
    server.login('lunmay24@gmail.com', password)

    msg = "\r\n".join([
    "From: lunmay24@gmail.com",
    "To: lunmay24@gmail.com",
    "Subject: NSE calls and Analysis at " + str(datetime.datetime.now()),
    "",
    "Sell : SBI @ 206.95 NSE, Buy : SBI @ 204.96 BSE"
    ])

    #try:
    server.sendmail('lunmay24@gmail.com','lunmay24@gmail.com',msg)
    print "Mail send successfully to lunmay24@gmail.com"
    server.close()
    #except:
    #   print "Mail not sent"

if __name__ == '__main__':
    pwd = base64.b64encode('kapkhovum')
    send_mail(pwd)