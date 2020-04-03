import re
import requests
import lxml
from bs4 import BeautifulSoup
#获取弹幕地址
url = input('请输入视频的URL：')
resp = requests.get(url)
match_rule = r'cid=(.*?)&aid'
oid = re.search(match_rule,resp.text).group().replace('cid=','').replace('&aid','')
print('弹幕编号为：',oid)
xml_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid='+oid
html = requests.get('https://api.bilibili.com/x/v1/dm/list.so?oid='+oid)
resp2 = BeautifulSoup(html.text,'lxml')  #解析后的页面文件
print('弹幕地址为：',html.url)
resp2 = resp2.encode("raw_unicode_escape").decode()
print('弹幕页内容：\n',resp2)
result = re.findall("\">(.*?)</d>",resp2)
print('正则后的纯弹幕内容：\n',result)
# 将弹幕写入danmu.log文件中，得先创建一个danmu.log文件，并与当前的py文件处在相同目录下
mylog = open('danmu.log',mode = 'a',encoding = 'utf-8')
for i in result:
    print(i,file = mylog)
mylog.close()
print('弹幕内容已打印在mylog.log文件中！')


