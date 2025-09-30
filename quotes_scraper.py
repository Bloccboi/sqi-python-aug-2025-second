import requests
from bs4 import BeautifulSoup
from collections import Counter

print("Getting quotes from website...")
response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.content, 'html.parser')


quotes = soup.find_all('div', class_='quote')
print(f"Found {len(quotes)} quotes!")


all_quotes = []
all_authors = []
all_tags = []

for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    
    all_quotes.append(text)
    all_authors.append(author)
    all_tags.extend(tags)

print(f"1. Total quotes: {len(all_quotes)}")

unique_authors = len(set(all_authors))
print(f"2. Unique authors: {unique_authors}")

author_counts = Counter(all_authors)
top_author = author_counts.most_common(1)[0]
print(f"3. Author with most quotes: {top_author[0]} ({top_author[1]} quotes)")

quotes_with_is = 0
for quote in all_quotes:
    if 'is' in quote.lower():
        quotes_with_is += 1
print(f"4. Quotes containing 'is': {quotes_with_is}")

tag_counts = Counter(all_tags)
print(f"5. Tags and their frequencies:")
for tag, count in tag_counts.items():
    print(f"   {tag}: {count}")

print("\Completed!")