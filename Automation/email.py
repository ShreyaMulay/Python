import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# from email import encoders


import smtplib,email,email.encoders,email.mime.text,email.mime.base


def MainSender(filename, time):
    try:
        fromAdd = "shreyamule17@gmail.com"
        toAdd = "shreyamule17@gmail.com"

        msg = MIMEMultipart()  # 1) multi purpose internet message 2) security purpose 3) send ascii data

        msg['From'] = fromAdd
        msg['To'] = toAdd

        body = f"""
        Hello {toAdd},
        Welcome to Marvelous InfoSystem.
        Running processes are attached to this email.
        Log file created at: {time}
        
        This is an auto-generated email.

        Thanks and regards,
        Shreya Mulay
        """

        subject = f"Process generated email {time}"

        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")

        part = MIMEBase('application', 'octet-stream')

        part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition', f"attachment; filename= {filename}")

        msg.attach(part)

        attachment.close()

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  
            server.login(fromAdd, "thgb styc aeoc qscc") 
            text = msg.as_string() 
            server.sendmail(fromAdd, toAdd, text)  

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

filename = "log.txt"
time = "2023-06-02 10:00:00"
MainSender(filename, time)
