import scrapper

import smtplib
import ssl

from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date


port = 465  # For SSL
context = ssl.create_default_context()

images_urls = scrapper.get_image_urls()

title = 'Fresh memes ' + str(date.today())

msg = MIMEMultipart('alternative')
msg['Subject'] = title
msg['From'] = Config.login
msg['To'] = Config.login

message = '<html><body><p>This is your daily portion of memes. Enjoy.<p>'
for url in images_urls:
    message += '''\
            <p>{0}</p>
            <img src="{0}">
    '''.format(url)
message += '</body></html>'

mail_body = MIMEText(message, 'html')
msg.attach(mail_body)
msg_to_str = msg.as_string()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(Config.login, Config.password)
    server.sendmail(Config.login, Config.login, msg_to_str)
