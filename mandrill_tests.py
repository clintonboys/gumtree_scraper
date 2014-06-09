import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')

msg['Subject'] = "Hello from Mandrill, Python style!"
msg['From']    = "John Doe <john@doe.com>" # Your from name and email address
msg['To']      = "cdsboys@gmail.com"

text = "Mandrill speaks plaintext"
part1 = MIMEText(text, 'plain')

html = "<em>Mandrill speaks <strong>HTML</strong></em>"
part2 = MIMEText(html, 'html')

username = os.environ['cdsboys@gmail.com']
password = os.environ['dZkyaV369DEIq05GtvpCJw']

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.mandrillapp.com', 587)

s.login(username, password)
s.sendmail(msg['From'], msg['To'], msg.as_string())

s.quit()