import requests
from bs4 import BeautifulSoup
import time
import random
from PIL import Image
import json


headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
'Cookie': 'PHPSESSID=51c37e9004302c8fe81a9c6fa8d4fff7'
}

def get_yzm():
    session=requests.session()
    url='http://www.af122.com/shdcpic/wz1/yyzm.php'
    r1=session.get(url=url,headers=headers)
    with open('yzm2.jpg','wb') as f:
        f.write(r1.content)
    img=Image.open('yzm2.jpg')
    img.show()
    return session

def get_Info():
    session=get_yzm()
    url='http://www.af122.com/shdcpic/wz1/deal1.php'
    data={
    'cp' : 'V137L9',
    'cj' : '622221 ',
    'cjz' : '126292 ',
    'jsz' :input('输入验证码:'),
    'code' : '011sed5T10VYn61Ps32T1CQ85T1sed5X'
    }
    r2=session.post(url=url,data=data,headers=headers)
    print(r2.content.decode('utf-8'))
get_Info()