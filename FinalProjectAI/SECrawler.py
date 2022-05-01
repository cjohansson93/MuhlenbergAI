"""
Christian Johansson
Artificial Intelligence, Final Project
5/1/2022
Professor Silveyra

"""

import requests
import re
import urllib
from bs4 import BeautifulSoup


def Crawler():
    stack = list()
    # Prevents infinity loops due to revisiting
    visited = list()
    # Stores total number of page links per page
    numPages = 0

    with open('PreviousCrawlPageNum.txt', 'r') as f:
        previousNum = int(f.read())
        if 0 < previousNum < 20000:
            numPages = previousNum
            with open('PreviousCrawlStack.txt', 'r', encoding='utf-8') as g:
                stack = g.read().split()

            with open('PreviousCrawlVisited.txt', 'r', encoding='utf-8') as h:
                visited = h.read().split()
        else:
            # Indicates starting page for crawl
            stack.append("https://www.muhlenberg.edu/")
    while len(stack) and numPages < 20000:
        r = requests.get(stack.pop())
        # Code 200 reflects a valid/unbroken link
        if r.status_code == 200:
            if r.url not in visited:
                visited.append(r.url)
                numPages += 1
                with open('PreviousCrawlStack.txt', 'w', encoding='utf-8') as f:
                    for i in stack:
                        f.write("{}\n".format(i))
                with open('PreviousCrawlVisited.txt', 'w', encoding='utf-8') as f:
                    for i in visited:
                        f.write("{}\n".format(i))
                with open('PreviousCrawlPageNum.txt', 'w', encoding='utf-8') as f:
                    f.write(str(numPages))
                # Prints number and URL for indication of page transversed
                print(str(numPages) + ": " + r.url)
                # Stores HTML page
                page = r.text
                soup = BeautifulSoup(page, 'html.parser')
                # Find valid URLS
                allLinks = re.findall(r'href="(.*?)"', page)
                # Sort out the absolute URLS (http, https, // <-- shortcut notation for abs)
                absLinks = [i for i in allLinks if i.startswith('http') or i.startswith('//')]
                # Sort relative links by remainder not in absLinks
                relLinks = [i for i in allLinks if i not in absLinks]
                # Cleaning out invalid crawl links (external sites, photos, videos, etc)
                internalLinks = [i for i in allLinks if not ((i.startswith('http') or i.startswith('//')) and "//www.muhlenberg.edu" not in i)]
                internalLinks = [i for i in internalLinks if i.endswith('/') or i.endswith(".htm") or i.endswith(".html")]
                # Patch relative links with the current URL so stack only has abs
                for link in internalLinks:
                    url = urllib.parse.urljoin(r.url, link)
                    # Remove anchors
                    url = url.split("#")[0]
                    if url not in visited and url not in stack:
                        stack.append(url)
                # Write to .txt file in directory 'Pages'
                # Each page has its URL written to pageX.txt
                # and word contents written to X.txt
                with open('Pages/page'+str(numPages)+'.txt', 'w', encoding='utf-8') as f:
                    f.write("{}\n".format(r.url))
                with open('Text/'+str(numPages)+'.txt', 'w', encoding='utf-8') as f:
                    f.write(soup.get_text())
                # Increment counter for each page


Crawler()
