import requests
import re
import urllib


def main():
    stack = list()
    visited = list()
    numPages = 0
    stack.append("https://www.muhlenberg.edu/")
    while len(stack):
        r = requests.get(stack.pop())
        if r.status_code == 200:
            if r.url not in visited:
                visited.append(r.url)
                numPages += 1
                print(str(numPages) + ": " + r.url)
                page = r.text
                # Find valid URLS
                allLinks = re.findall(r'href="(.*?)"', page)
                absLinks = [i for i in allLinks if i.startswith('http') or i.startswith('//')]
                relLinks = [i for i in allLinks if i not in absLinks]
                absCount = len(absLinks)
                relCount = len(relLinks)
                internalLinks = [i for i in allLinks if not ((i.startswith('http') or i.startswith('//')) and "//www.muhlenberg.edu" not in i)]
                internalLinks = [i for i in internalLinks if i.endswith('/') or i.endswith(".htm") or i.endswith(".html")]
                for link in internalLinks:
                    url = urllib.parse.urljoin(r.url, link)
                    if url not in visited and url not in stack:
                        stack.append(url)
                with open('Pages/page'+str(numPages)+'.txt', 'w', encoding='utf-8') as f:
                    f.write("{}\n".format(r.url))
                    f.write("{}\n".format(relCount))
                    f.write("{}\n".format(absCount))
                    f.write(page)


main()
