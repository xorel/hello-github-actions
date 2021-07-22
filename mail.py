#!/usr/bin/env python3

import smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 587  # For starttls
smtp_server = 'smtp.dreamhost.com'
sender_email = 'infra@opennebula.org'
receiver_email = 'jorel@opennebula.io'
password = sys.argv[1]

message = MIMEMultipart('text')
message["Subject"] = "python multipart"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
here
is
something
"""

part1 = MIMEText(text, "plain")

message.attach(part1)

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo('127.0.0.1')  # Can be omitted

    server.starttls(context=context)

    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.close()

print("OK")
