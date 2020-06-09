#!/usr/bin/env python3

import requests
import logging
import configparser
import smtplib
from email.message import EmailMessage
import os
from datetime import date
import time

def send_warning_email(to_email, server, port, from_email, password, message_content):
    print('email to Tanja has been sent on {}.'.format(date.today()))

    # Create the message
    subject = 'Daily message from Francesco'
    text = message_content
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Open communication and send
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

def read_config(config_file):
    config = configparser.ConfigParser()
    with open(config_file, 'r') as conf:
        config.read_file(conf)
    return config


def main():

    LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
    LOG_LEVEL = logging.ERROR

    logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, filename="./logs.log")

    try:
        response = requests.get("https://meinbio-symposium.herokuapp.com/")
        if response.status_code != 200:
            config = read_config("g")
            send_warning_email("francesco.ferrari.1988@gmail.com",
                                server=config['DEFAULT']['server'],
                                port=config['DEFAULT']['port'],
                                from_email=config['DEFAULT']['email'],
                                password=config['DEFAULT']['password'],
                                message_content = "The website did not return a 200 status code")
    except Exception as exp:
        logging.exception("An error occured")
        config = read_config("/Users/ferrari/scripts_bin/email_conf.ini")
        send_warning_email("francesco.ferrari.1988@gmail.com",
                            server=config['DEFAULT']['server'],
                            port=config['DEFAULT']['port'],
                            from_email=config['DEFAULT']['email'],
                            password=config['DEFAULT']['password'],
                            message_content = "An Exception occurred while trying to reach the website")

    n_lines_log = int(os.popen("wc -l logs.log").read().split()[0])
    if n_lines_log > 10:
        os.remove("logs.log")


def send_email_Tanja():
    tanja = "tanja.vogel@anat.uni-freiburg.de"
    francesco = "ferrari@ie-freiburg.mpg.de"
    while True:

        config = read_config("email_conf.ini")
        send_warning_email(tanja,
                            server=config['DEFAULT']['server'],
                            port=config['DEFAULT']['port'],
                            from_email=config['DEFAULT']['email'],
                            password=config['DEFAULT']['password'],
                            message_content = 
"""
Dear Tanja,

Today, {today}, I will be working at Albertstrasse 23, from 9:30 am. to  
17:30 pm.

Best,

Francesco 

""".format(today=date.today())     
                )

        time.sleep(86400)

if __name__ == "__main__":
    send_email_Tanja()
    # main()
