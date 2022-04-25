"""
Christian Johansson
Artificial Intelligence, Homework 7
4/24/2022
Professor Silveyra
This file is a website crawler, gathering all links, and counting them on a site. Then valid links
are from that page and so on. Each page has its URL, number of relative and absolute link counts and
complete HTML written to a .txt file
"""

import requests
import re
import urllib


def main():
    stack = list()
    # Prevents infinity loops due to revisiting
    visited = list()
    # Stores total number of page links per page
    numPages = 0
    counter = 0
    # Indicates starting page for crawl
    stack.append("https://www.muhlenberg.edu/")
    while len(stack) and counter < 500:
        r = requests.get(stack.pop())
        # Code 200 reflects a valid/unbroken link
        if r.status_code == 200:
            if r.url not in visited:
                visited.append(r.url)
                numPages += 1
                # Prints number and URL for indication of page transversed
                print(str(numPages) + ": " + r.url)
                # Stores HTML page
                page = r.text
                # Find valid URLS
                allLinks = re.findall(r'href="(.*?)"', page)
                # Sort out the absolute URLS (http, https, // <-- shortcut notation for abs)
                absLinks = [i for i in allLinks if i.startswith('http') or i.startswith('//')]
                # Sort relative links by remainder not in absLinks
                relLinks = [i for i in allLinks if i not in absLinks]
                absCount = len(absLinks)
                relCount = len(relLinks)
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
                # Each page has its URL, number of relative and absolute link counts and
                # complete HTML written to a .txt file
                with open('Pages/page'+str(numPages)+'.txt', 'w', encoding='utf-8') as f:
                    f.write("{}\n".format(r.url))
                    f.write("{}\n".format(relCount))
                    f.write("{}\n".format(absCount))
                    f.write(page)
                # Increment counter for each page
                counter += 1


main()
