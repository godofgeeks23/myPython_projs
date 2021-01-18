# This sends an email to a particular email id
import smtplib
import ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "devaviral2307@gmail.com"
receiver_email = "aviralji4@gmail.com"
password = "justfordev"
message = """\
Subject: Hi Aviral!

This message is sent from your Python Bot.
Have a nice day!
- Python.
"""
print("Sending EMail to " + receiver_email + "...")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print("EMail sent successfully!")
