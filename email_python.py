import smtplib, ssl
import time
from datetime import date
import datetime
from email.message import EmailMessage
import os

def send_email_T():

    print('email to T sent on {}'.format(date.today()))

    port = 465
    password = os.environ.get('PASSEMAILFRANFERR88')

    tanja_email = "tanja.vogel@anat.uni-freiburg.de"
    test_email = "francesco.ferrari.1988@gmail.com"

    sender_email = test_email
    receiver_email = [tanja_email]
    subject = "Daily email from Francesco"
    message = """\
Dear Tanja,

Today, {today}, I will be working at Albertstrasse 23, from 9:30 am. to 17:30 pm.

Work will include cell culture and bioinfo analysis.

Best,

Francesco 

    """.format(today=date.today())   

    text = message
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['CC'] = "ferrari@ie-freiburg.mpg.de"

    ### CREATE A SECURE SSL CONTEXT
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("francesco.ferrari.1988@gmail.com",password)
        server.send_message(msg)

if __name__ == "__main__":
    
    while True:
        day_of_the_week = datetime.datetime.today().weekday()
        if day_of_the_week != 5 and day_of_the_week != 6: 
            send_email_T()
        time.sleep(86400)
