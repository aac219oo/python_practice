import requests, time
from bs4 import BeautifulSoup
#建立日期時間檔名資訊
now = time.strftime("%Y-%m%d_%H%M%S", time.localtime())

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
website = 'https://www.ptt.cc'
web = requests.get(url, cookies={'over18':'1'})
#print(web.text)
soup = BeautifulSoup(web.text, "html.parser") #HTML 解析
titles = soup.find_all('div', class_='title') #抓出 DIV 標籤 class = title 的原始碼
authors = soup.find_all('div', class_='author') #抓出 DIV 標籤 class = title 的原始碼
#print(titles[0])
#print(authors[0].text)
output = ''
k = 0
for i in titles:
    if i.find('a') != None:                           # 判斷如果不為 None
        #print(i.find('a').get_text())                 # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        #print(website + i.find('a')['href'], end='\n\n')  # 使用 ['href'] 取得 href 的屬性
        output += i.find('a').get_text() + '\n' + website + i.find('a')['href'] + '\n' + authors[k].text +'\n\n'
        k += 1
        
f = open('website_' + now + '.txt','w')   # 建立並開啟純文字文件
f.write(output)     # 將資料寫入檔案裡
f.close()
