# this fetches the active corona updates from the MHFW website and sends an email of the data
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
import smtplib
import ssl


def extract_contents(row): return [x.text.replace('\n', '') for x in row]


URL = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed',
                 'Foreign-Confirmed', 'Cured', 'Death']
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if stat:
        if len(stat) == 5:
            # last row
            stat = ['', *stat]
            stats.append(stat)
        elif len(stat) == 6:
            stats.append(stat)
stats[-1][1] = "Total Cases"
stats.remove(stats[-1])
objects = []
for row in stats:
    objects.append(row[1])
y_pos = np.arange(len(objects))
performance = []
for row in stats:
    performance.append(str(row[2]) + str(row[3]))
table = tabulate(stats, headers=SHORT_HEADERS)
print("Got the latest corona updates...")
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "devaviral2307@gmail.com"
receiver_email = ["aviralji4@gmail.com", "aviralji2307@gmail.com",
                  "aakashsrivastava854@gmail.com", "aakash.srivastav385@gmail.com",
                  "arvindsrivaatava@gmail.com", "saritasri1805@gmail.com"]
password = "justfordev"
message = """\
Subject: CORONA UPDATE!

""" + table + """ - Python."""
print("Sending EMails...")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for x in range(len(receiver_email)):
        server.sendmail(sender_email, receiver_email[x], message)
        print("EMail successfully sent to " + receiver_email[x])
print("All EMails were sent successfully!")
