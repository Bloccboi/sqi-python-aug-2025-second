import requests

from bs4 import BeautifulSoup

url = "https://landwey.ng"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
with open("landwey_page.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
print("\nPage source saved to 'landwey_page.html'")
