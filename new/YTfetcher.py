from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs


print("Working...")

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

response = HTMLSession().get(url)
response.html.render(timeout=60)
soup = bs(response.html.html, "html.parser")

title = soup.find("meta", itemprop="name")['content']
views = soup.find("meta", itemprop="interactionCount")['content']
date_pub = soup.find("meta", itemprop="datePublished")['content']
duration = soup.find("span", {"class": "ytp-time-duration"}).text

print(f"Title: {title}")
print(f"Views: {views}")
print(f"Published at: {date_pub}")
print(f"Video Duration: {duration}")
