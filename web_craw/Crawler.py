import urllib.request as req
webroot = 'https://www.ptt.cc'
url="https://www.ptt.cc/bbs/basketballTW/index.html"
request = req.Request(url, headers={"User-Agent":
                                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)
        print(webroot + title.a['href'])
