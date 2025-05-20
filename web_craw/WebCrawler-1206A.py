import sys, requests, json, os, wget, time

#取代違法字源的方法
def text_cleanup(text):
    new =""
    for i in text:
        if i not in'\?.!/;:"':
            new += i
    return new

print("開始爬蟲")
 
#偽裝成瀏覽器
# 利用get取得API資料  
#url = "https://www.dcard.tw/_api/forums/pet/posts?popular=true"  #舊版 API
url = "https://www.dcard.tw/service/api/v2/posts?popular=false" #新版 API
reqs = requests.get(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
#print(reqs.status_code) #503 錯誤 // 200等於正常// 403 限制存取
'''#暫時手動繞過 recaptcha 的認證
if(int(reqs.status_code)==200):
    print("Dcard伺服器狀態:連線中")
else:
    print("Dcard伺服器狀態:拍謝失敗捏")
    print(reqs.status_code)
    os.system("pause")
    os._exit()
'''
#利用json.loads()解碼JSON
#reqsjson = json.loads(reqs.text)

f = open("DcardTest.txt", "r+", encoding='utf-8-sig') #以人工方式搬 JSON 做應用
JSONstring = f.read()
reqsjson = json.loads(JSONstring)

#取得篇數
total_num = len(reqsjson)

for i in range(total_num):
    title = reqsjson[i]["title"] #取得每篇標題
    title = text_cleanup(title) #標題會有非法字元要去掉
    media_num = len(reqsjson[i]['media']) #判斷這文章圖的數量
    print("第" + str(i) + "篇....正在檢查有沒有圖檔~")
    if media_num != 0:
        path =  title #資料夾名字用文章標題命名
        print("此篇狀態：有圖檔^_^")
        if not os.path.isdir(path):  #檢查是否已經有了
            os.mkdir(path) #沒有的用標題建立資料夾
        for i_m in range(media_num):
            image_url = reqsjson[i]['media'][i_m]['url']
            if ('vivid.dcard.tw' not in image_url):
                filepath =  title + '/' + str(i_m) + '.jpg'
                if not os.path.isfile(filepath): #檢查是否下載過圖片，沒有就下載
                    print(image_url)
                    wget.download(image_url, filepath)
        print("完成此篇文章的圖片抓取。")
    else:
        print("此篇狀態：沒有圖QQ")
    






