import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.uk.xensource.com')
s.set_debuglevel(1)
msg = MIMEText("""body""")
sender = 'me@example.com'
recipients = ['john.doe@example.com', 'john.smith@example.co.uk']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())