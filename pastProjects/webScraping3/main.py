# this fetches the active corona updates from the MHFW website
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt


def extract_contents(row): return [x.text.replace('\n', '') for x in row]


URL = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['SNo', 'State', 'Indian-Confirmed',
                 'Foreign-Confirmed', 'Cured', 'Death']
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))
stats = []
all_rows = soup.find_all('tr')
print("CORONA UPDATE!")
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
print(table)
