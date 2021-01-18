# gets all the headings of a particular class in a web page
import requests
import bs4
res = requests.get(
    'https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('.mw-headline')
for i in hi:
    print("Heading: " + i.getText())
