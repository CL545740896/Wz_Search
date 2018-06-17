import requests
from bs4 import BeautifulSoup
import time
import random
from PIL import Image
import json
'''
车主服务查询接口
'''
'''
验证码ID  1529197783611 毫秒时间戳
          1529197370715
'''

headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 micromessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        'Cookie': 'userId=openId=oBFR-wsust_8tfy4dX9jlxjvHOEU&unionId=oZFU2xGoT9y-1fiNS1Rfq3zJrDj0; ASP.NET_SessionId=dfpjdtoqgyz2t2hctkz4webb',
        'Connection': 'keep-alive'
    }

def get_yazm():
    '''
    获取验证码
    :return: 
    '''
    t=str(round(time.time() * 1000))
    url='http://sms.czfw.cn/vio/Service/AuthCode.ashx?id={}'.format(t)
    session=requests.session()
    r1=session.get(url=url,headers=headers)
    with open('yzm.jpg','wb') as f:
        f.write(r1.content)
    img = Image.open('yzm.jpg')
    img.show()
    return t,session


def get_parms(CAR_NO,FDJH):
    '''
    获取查询参数
    :param CAR_NO: 
    :param FDJH: 
    :return: 
    '''
    url='http://sms.czfw.cn/vio/Service/HandServer.ashx?Method=checkwfcx'
    t,session=get_yazm()
    data={
        'hphm':CAR_NO,
        'hpzl': '02',
        'nf': '1',
        'fdjh': FDJH,
        'nv': '0',
        'vin': '',
        'unionId':'oZFU2xGoT9y-1fiNS1Rfq3zJrDj0',
        'sessionID':t,
        'yzmcode':input('输入验证码:'),
    }
    print(data)
    r1=session.post(url=url,data=data,headers=headers)
    json_data=json.loads(r1.content.decode('utf-8'))
    print(json_data)
    if 'sign' in json_data:
        return session,json_data['ts'],json_data['sign'],t
    else:
        print('验证码输入错误,重新输入')
        return get_parms(CAR_NO=CAR_NO,FDJH=FDJH)



def getInfo(CAR_NO,FDJH):
    '''
    获取查询信息
    :param CAR_NO: 
    :param FDJH: 
    :return: 
    '''
    openid=str(random.randint(1,100000000))
    unionId=str(random.randint(1,100000000))

    session,ts,sign,sessionid=get_parms(CAR_NO=CAR_NO,FDJH=FDJH)
    data={
        'rdohpzl': '02',
        'vehfdjh': FDJH,
        'sessionID': sessionid,
        'hphm':CAR_NO,
        'needfdjh': '1',
        'needvin': '0',
        'flag': '1',
        'unionId': unionId,
        'openId': openid,
        'ts': ts,
        'sign': sign,
    }
    url='http://sms.czfw.cn/vio/wfxx.aspx'
    r1=session.post(url=url,data=data,headers=headers)
    html=r1.content.decode('utf-8')
    parse_html(html=html)

def parse_html(html):
    '''
    解析源码
    :param html: 
    :return: 
    '''
    soup = BeautifulSoup(html, 'html.parser')
    times = soup.find('time').text.replace(" ", "")
    points = soup.find('div', attrs={'class': 'points'}).text.replace(" ", "")
    art = soup.find('div', attrs={'class': 'art-btm'}).text.replace(" ", "")
    main = soup.find('div', attrs={'class': 'main'}).text.replace(" ", "")
    print('车辆信息 : ' + times)
    print('扣除分数 : ' + points)
    print('总共记录 : ' + art)
    print('记录详情 : ')
    if '违法记录哦' in main:
        print(main)
    else:
        mains = str(main.strip()).split('理')
        for items in mains:
            result = items[2:3] + '月' + items[0:2] + '日'
            for info in items[4:]:
                result = result + info
            if items != '':
                print(result + '理')



if __name__ == '__main__':
    search_list = [
       #查询列表
    ]
    for items in search_list:
        FDJH = items[1]
        length = len(FDJH)
        getInfo(CAR_NO=items[0].strip(), FDJH=(FDJH[length - 4:length]).strip())
