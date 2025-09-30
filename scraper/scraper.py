# import string

# from datetime import datetime

import requests

from bs4 import BeautifulSoup

url = "https://sqi.edu.ng/"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops! Something went wrong. Check your internet connection and try again: {e}")
else:
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        with open("sqi-homepage.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
    else:
        soup = BeautifulSoup(response.text, 'html.parser')

        print("Unexpected response:")
        print(f"Status Code: {response.status_code}")
        with open("unexpected_reponse.html", "w") as f:
            f.write(soup.prettify())
        print("Check 'unexpected_reponse.html' for more details" )


# 1. Create the project folder
# 2. Create a virtual environment
# 3. Activate the virtual environment
# 4. Install dependencies
# 5. Scrape the site of your choice.