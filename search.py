#! python3
# search.py - Opens several search results

import requests, sys, webbrowser, bs4

print('Searching...') # display text while loading the pages
res = requests.get("https://www.google.com/search?q=" + ' '.join(sys.argv[1:]), 'html.parser')
print(sys.argv[1])
res.raise_for_status()

# Retrieve top results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open tabs of search results automatically
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://www.google.com' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)