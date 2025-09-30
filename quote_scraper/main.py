from collections import Counter

import requests

from bs4 import BeautifulSoup

# important

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Something went wrong. Check your internet connection?")
    print("More details:")
    print(e)
else:
    status_code = response.status_code
    if status_code != 200:
        print(f"Status Code: {status_code}")
        print("Unexpected response:")
        print(response.text)
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Number 1
        quotes_divs = soup.select('div.quote')
        print(f"Number of quotes: {len(quotes_divs)}")

        # Number 2
        authors_small = soup.select("div.quote > span:nth-child(2) > small")
        authors = [author_small.text for author_small in authors_small]
        print(f"Number of unique authors: {len(set(authors))}")

        # Number 3
        authors_nos_of_quotes = dict(Counter(authors))
        author_with_most_quotes = max(authors_nos_of_quotes, key=authors_nos_of_quotes.get)
        print(f"Author with the most quotes: {author_with_most_quotes}")

        # Number 4
        quotes_spans = soup.select('div.quote span.text')
        no_of_quotes_with_is = sum(["is" in quote_span.text.lower() for quote_span in quotes_spans])
        print("No of quotes that contain the word “is”:", no_of_quotes_with_is)

        a_tags = soup.select('div.quote div.tags a.tag')
        tags = [a_tag.text for a_tag in a_tags]
        print(tags)
        for tag, occurence in dict(Counter(tags)).items():
            print(f"{tag} -> {occurence}")
