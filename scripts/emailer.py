import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

msg = MIMEMultipart()

me = 'dxgovbot@gmail.com'
receipients = ['d@ve.gl']
to = ', '.join(receipients)

date = datetime.now().strftime("").strftime("%d %b")

msg['Subject'] = 'DXgov digest ' + date
msg['From'] = me
msg['To'] = to

msg = MIMEText("Test email")

msg.preamble = 'Your daily DXdao digest.'

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(me, os.getenv('GMAIL_AUTH'))
s.sendmail(me, receipients, msg.as_string())