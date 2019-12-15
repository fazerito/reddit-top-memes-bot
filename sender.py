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

message = '<html><body>'
for url in images_urls:
    message += '''\
        <p>This is an HTML body.<br>
            It also has an image.
            </p>
            <img src="{}">
    '''.format(url)
message += '</body></html>'

mail_body = MIMEText(message, 'html')

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(Config.login, Config.password)
    server.sendmail(Config.login, Config.login, message)
