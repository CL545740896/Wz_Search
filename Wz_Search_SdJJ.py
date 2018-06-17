import requests
from bs4 import BeautifulSoup
import re
import time
import random
log=open('log.txt','a+')
error=open('error.txt','a+')
def get_html(CAR_NO,FDJH):
    try:
        time.sleep(3)

        openid=str(random.randint(1,100000000))
        data={
            'hphm':CAR_NO,
              'hpzl':'02',
              'fdjh':FDJH,
              'openId' : openid,
        }
        head={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 micromessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
            'Cookie': 'tpdyhopenId={}'.format(openid),
            'Connection': 'keep-alive'
        }
        session=requests.session()
        r1=session.request('Post','http://sms.czfw.cn/tpdyh/Service/HandServer.ashx?Method=checkwfcx',data=data,headers=head)
        r_json=r1.json()
        print(r_json)
        if r_json.get('flag')==-1:
            error.write(CAR_NO +'-'+FDJH+'\n')
            session.close()
            return None
        data['ts']=r_json.get('ts')
        data['sign']=r_json.get('sign')
        print(r1.status_code)
        r2=session.request('Post','http://sms.czfw.cn/tpdyh/wzz/wfxx.aspx',data=data,headers=head)
        soup = BeautifulSoup(r2.content.decode('utf-8'),'html.parser')
        times = soup.find('time').text.replace(" ", "")
        points = soup.find('div', attrs={'class': 'points'}).text.replace(" ", "")
        art = soup.find('div', attrs={'class': 'art-btm'}).text.replace(" ", "")
        main = soup.find('div', attrs={'class': 'main'}).text.replace(" ", "")
        session.close()
        return (times.strip(), points.strip(), art.strip(),main.strip())
    except Exception as e:
        error.write(str(e)+'\n')
        error.write(CAR_NO+'-'+FDJH + '\n')
        print('超时')  #超时连接重新获取
        print(e)
        print(CAR_NO,FDJH)
        get_html(CAR_NO,FDJH)




if __name__ == '__main__':
    search_list = [
        #查询列表
    ]
    for items in search_list:
        FDJH=items[1]
        length=len(FDJH)
        info=(get_html(CAR_NO=items[0].strip(), FDJH=(FDJH[length-4:length]).strip()))
        if info:
            times, points, art,main=info
            log.write('车辆信息 : '+times+'\n')
            log.write('扣除分数 : '+points + '\n')
            log.write('总共记录 : '+art+ '\n')
            log.write('记录详情 : '+ '\n')
            print('车辆信息 : '+times)
            print('扣除分数 : '+points)
            print('总共记录 : '+art)
            print('记录详情 : ')
            if '违法记录哦' in main:
                log.write(main+'\n')
                print(main)
            else:
                mains=str(main.strip()).split('理')
                for items in mains:
                    result=items[2:3]+'月'+items[0:2]+'日'
                    for info in items[4:]:
                        result=result+info
                    if items !='':
                        print(result+'理')
                        log.write(result+'\n')
            print('\n')
            log.write('\n')