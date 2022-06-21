# 使用 requests 工具
from bs4 import BeautifulSoup
import requests as req

# # 使用 json 工具
# import json

# r = req.get('https://httpbin.org/get')
# #狀態碼
# print(r.status_code)

# #資料編碼
# print (r.encoding)
# #網頁原始碼
# print(r.text)

# #GET
# #query string 請求回傳資料
# #pamas 參數
# my_parmas={
#     'key1': 'value1', 
#     'key2': 'value2'
# }

# r=req.get('https://tw.op.gg/champions/twitch/adc/build?region=kr&tier=platinum_plus',params=my_parmas)
# print(r.text)

# print(r.url)

# #POST
# my_datas={
#     'key1': 'value1', 
#     'key2': 'value2'
# }

# r=req.post('https://tw.op.gg/champions/twitch/adc/build?region=kr&tier=platinum_plus',data=my_datas)
# print(r.text)

from bs4 import BeautifulSoup as bs
# url='https://store.line.me/stickershop/product/26229/zh-Hant?utm_source=gnsh_stickerDetail'

# r=req.get(url)
# s=BeautifulSoup(r.text,'lmxl')
# print

from bs4 import BeautifulSoup as bs
import requests as req
my_cookies = {
    "over18": "1"
}
url='https://www.ptt.cc/bbs/sex/index.html'
res=req.get(url,cookies=my_cookies)
soup = bs(res.text, "lxml") 
#print(res.text)
for i in soup.select('div.r-ent div.title a'):
         print(i.get_text())
         print(i['href'])

         