#! python3
# search.py - Opens several search results

import requests, sys, webbrowser, bs4

print('Searching...') # display text while loading the pages
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top results
#TODO: Open tabs of search results automatically