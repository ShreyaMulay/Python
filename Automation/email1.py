import re
import smtplib
import urllib.request as urllib2
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def sendmailToPariticipant(UserName,Password,To_FileName,Attachment):
    ToList = To_FileName
    
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "Meeting Reminder"
        body = f"Hello {UserName},\n\nThis is a reminder for our upcoming meeting.\n\nBest regards,\nShreya Mulay"

        msg.attach(MIMEText(body, 'plain'))

        
        email_text = msg.as_string()
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(UserName,Password)

        server.sendmail(UserName,ToList,email_text)
    
    except Exception as E:
        print("Exception occured",E)



sendmailToPariticipant('shreyamule17@gmail.com','tcfy rwdc zkbo wsca','shreyamule17@gmail.com','')