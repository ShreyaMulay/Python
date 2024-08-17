import re
import smtplib
import urllib.request as urllib2
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def is_connected():
	try:
		urllib2.urlopen("https://mail.google.com/mail/u/0/",timeout = 10)
		return True
	except Exception as err:
		print("not connected",err)
		return False

def findemail(To_FileName):
    fd = open(To_FileName,"r")
    data = fd.read()
    fd.close()
    
    List = re.findall(r'\S+@\S+', data)
    return List

def sendmail(UserName,Password,To_FileName,Attachment):
    if(os.path.exists(To_FileName) and os.path.exists(Attachment)):
        ToList = findemail(To_FileName)
        # ToList = To_FileName

        print("::ToList",ToList)
        filename = Attachment
        
        try:
            msg = MIMEMultipart()
            msg['Subject'] = "Gentle Reminder .."
            
            attachment = open(filename, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p) 
            p.add_header('Content-Disposition', "attachment filename= %s" % filename)   
            msg.attach(p)
            
            email_text = msg.as_string()
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.ehlo()
            server.login(UserName,Password)

            server.sendmail(UserName,ToList,email_text)
        
        except Exception as E:
            print("Exception occured",E)



def sendmailToPariticipant(UserName,Password,To_FileName,Attachment):
    ToList = To_FileName

    print("::ToList",ToList)
    # filename = Attachment
    
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "Meeting Reminder"
        body = f"Hello {UserName},\n\nThis is a reminder for our upcoming meeting.\n\nBest regards,\nShreya Mulay"

        
        # attachment = open(filename, "rb")
        # p = MIMEBase('application', 'octet-stream')
        # p.set_payload((attachment).read())
        # encoders.encode_base64(p) 
        # p.add_header('Content-Disposition', "attachment filename= %s" % filename)   
        # msg.attach(p)
        msg.attach(MIMEText(body, 'plain'))

        
        email_text = msg.as_string()
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.ehlo()
        server.login(UserName,Password)

        server.sendmail(UserName,ToList,email_text)
    
    except Exception as E:
        print("Exception occured",E)



