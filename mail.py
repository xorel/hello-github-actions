#!/usr/bin/env python3

import smtplib, ssl, sys


port = 587  # For starttls
smtp_server = 'mail.opennebula.org'
sender_email = 'infra@opennebula.org'
receiver_email = 'jorel@opennebula.io'
password = sys.argv[1]

message = """\
Subject: Test email1

This message is sent from Python."""

#context = ssl.create_default_context()
context = ssl._create_unverified_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted

    server.starttls(context=context)

    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print("OK")
