import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Security footage'
msg['From'] = 'Security team'
msg['To'] = 'beepurush@gmail.com'

with open('EmailTemplate.txt') as my_file:
    data = my_file.read()
    msg.set_content(data)

with open('25-02-2022-15-06-06.mp4', "rb") as f:
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype="application", subtype=".mp4", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('pytest764@gmail.com', 'nymwxdkjuujklvsh')
    server.send_message(msg)

print('Email sent')
