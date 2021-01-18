# gets the title of a web page
import requests
import bs4
res = requests.get(
    'https://www.google.com/search?client=firefox-b-d&q=corona+update')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('title')
print("Page Title: " + hi[0].getText())
