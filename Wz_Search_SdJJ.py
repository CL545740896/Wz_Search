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
        ('鲁V137L9', '	622221'),
        ('鲁RMU253', '	210007492'),
        ('鲁RK879H', '	496347'),
        ('鲁RJ989E', '	376413'),
        ('鲁RJ989E', '	376413'),
        ('鲁RH818G', '	270318'),
        ('鲁R657CE', '	481048'),
        ('鲁R1E56G', '	003704'),
        ('鲁R09Y81', '	021529'),
        ('鲁R09V70', '	020580'),
        ('鲁QX7H75', '	100923'),
        ('鲁QRA957', '	785554'),
        ('鲁QR8T95', '	A63355'),
        ('鲁QQ95G1', '	B61761'),
        ('鲁QJ21B1', '	269579'),
        ('鲁QBB305', '	970037'),
        ('鲁QA982D', '	052509'),
        ('鲁Q63R23', '	913586'),
        ('鲁P3838L', '	017154'),
        ('鲁P185NZ', '	183272'),
        ('鲁NHJ186', '	M00326'),
        ('鲁N7107X', '	VA02H010937'),
        ('鲁N35F89', '	512682'),
        ('鲁MUR777', '	383425'),
        ('鲁M153V1', '	MG2252'),
        ('鲁LX8605', '	100477'),
        ('鲁L9Q796', '	A53860'),
        ('鲁KFK757', '	D05082'),
        ('鲁K08555', '	CG6089'),
        ('鲁JZM697', '	830065'),
        ('鲁JSL186', '	612463'),
        ('鲁J3991H', '	514452'),
        ('鲁HXF735', '	222747'),
        ('鲁HX111P', '	463032'),
        ('鲁HL275C', '	016165'),
        ('鲁HL275C', '	016165'),
        ('鲁HL275C', '	016165'),
        ('鲁HF281K', '	63E087'),
        ('鲁HF180N', '	420297'),
        ('鲁HD125Z', '	663604'),
        ('鲁HD125Z', '	663604'),
        ('鲁HD125Z', '	663604'),
        ('鲁HA757G', '	021105'),
        ('鲁H7G256', '	T17094'),
        ('鲁GL565Q', '	C82920873'),
        ('鲁GK652S', '	22991W'),
        ('鲁GK652S', '	22991W'),
        ('鲁GK652S', '	22991W'),
        ('鲁GD9X02', '	392226'),
        ('鲁GD861R', '	013402'),
        ('鲁GD053K', '	G00812'),
        ('鲁FF782X', '	110941'),
        ('鲁FF11999', '002734'),
        ('鲁F597A9', '	B08728'),
        ('鲁E7608G', '	527567'),
        ('鲁E7608G', '	527567'),
        ('鲁E2T082', '	238910'),
        ('鲁DGH036', '	035274'),
        ('鲁D980C0', '	086749'),
        ('鲁D980C0', '	086749'),
        ('鲁D2T356', '	410717'),
        ('鲁CTG507', '	HB1909'),
        ('鲁CAQ899', '	T91927'),
        ('鲁C3Y518', '	610424'),
        ('鲁BS286G', '	2007267'),
        ('鲁BK82R3', '	1505104694'),
        ('鲁BE51R7', '	801360'),
        ('鲁BD11376', '602601'),
        ('鲁BD02111', '901914'),
        ('鲁B9X1C3', '	556379'),
        ('鲁B9S96Y', '	AD33DG09240042'),
        ('鲁B9S57N', '	BD33DG09282366'),
        ('鲁B9S08N', '	AD33DG09210058'),
        ('鲁B9M1J5', '	553592'),
        ('鲁B8V9Z2', '	556238'),
        ('鲁B8V3Z0', '	555139'),
        ('鲁B8S93S', '	AD33DG09240028'),
        ('鲁B8S85G', '	AD33DG09030006'),
        ('鲁B8S65S', '	AD33DG09210041'),
        ('鲁B8S65G', '	AD33DG09170049'),
        ('鲁B8S57G', '	AD33DG07100050'),
        ('鲁B8S30S', '	BD33DG09062030'),
        ('鲁B8S28S', '	AD33DG09170008'),
        ('鲁B8HV83', '	E08209'),
        ('鲁B88TR5', '	543838'),
        ('鲁B88TQ0', '	276848'),
        ('鲁B87HN1', '	500694'),
        ('鲁B82EB3', '	Bm0302'),
        ('鲁B7X9R9', '	549200'),
        ('鲁B7S2A1', '	555429'),
        ('鲁B7S05L', '	BD33DG11032081'),
        ('鲁B7P83G', '	010998'),
        ('鲁B7P83G', '	010998'),
        ('鲁B7P7Q9', ' 554999'),
        ('鲁B7P18T', '	AD33DG06130710'),
        ('鲁B79XQ9', '	554590'),
        ('鲁B77XK8', '	517077'),
        ('鲁B71WG2', '	556914'),
        ('鲁B70KL7', '	544077'),
        ('鲁B6P0U0', '	552999'),
        ('鲁B60LT5', '	857407'),
        ('鲁B56ZH8', '	0079198'),
        ('鲁B56WH8', '	554257'),
        ('鲁B55XZ7', '	543121'),
        ('鲁B53VY9', '	550920'),
        ('鲁B52QQ2', '	622279'),
        ('鲁B52DF5', '	000879'),
        ('鲁B51SW0', '	549486'),
        ('鲁B50JR3', '	549478'),
        ('鲁B3P98V', '	AD33DG10170046'),
        ('鲁B3M9E8', '	556825'),
        ('鲁B3E77E', '	BD33DG05250974'),
        ('鲁B38XY1', '	L372734'),
        ('鲁B38GY8', '	544406'),
        ('鲁B36LM8', '	B56939'),
        ('鲁B35YN0', '	529787'),
        ('鲁B35YN0', '	529787'),
        ('鲁B35RZ2', '	529865'),
        ('鲁B30YN1', '	529940'),
        ('鲁B2Y2C5', '	L372834'),
        ('鲁B2L1A8', '	550047'),
        ('鲁B2A1A1', '	55B30A'),
        ('鲁B28XZ0', '	556820'),
        ('鲁B25MD2', '	550840'),
        ('鲁B23ZD0', '	556733'),
        ('鲁B23ZD0', '	556733'),
        ('鲁B1X70A', '	224153'),
        ('鲁B1S92L', '	BD33DG10252195'),
        ('鲁B1S79L', '	AD33DG10140037'),
        ('鲁B1S66R', '	AD33DG10150031'),
        ('鲁B17HF2', '	543888'),
        ('鲁B158LP', '	012857'),
        ('鲁B0S96G', '	AD33DG08310002'),
        ('鲁B0M7A2', '	554216'),
        ('鲁B0M5A5', '	133778'),
        ('鲁B0M5A5', '	133778'),
        ('鲁B06TS1', '	544390'),
        ('鲁B03WV1', '	555690'),
        ('鲁B03EG8', '	165720'),
        ('鲁B02FG5', '	F00627'),
        ('鲁AX811C', '	090891'),
        ('鲁AW1Y56', '	013878'),
        ('鲁AW1Y56', '	013878'),
        ('鲁AP889D', '	006432'),
        ('鲁AN10F1', '	310385'),
        ('鲁AMK285', '	E17766'),
        ('鲁AK3H86', '	624160'),
        ('鲁AK0W17', '	027538'),
        ('鲁AD01353', 'B00264'),
        ('鲁AB70S9', '	620423'),
        ('鲁AA9S17', '	22D926'),
        ('鲁A800N1', '	B11300'),
        ('鲁A717AJ', '	935933'),
        ('鲁A717AJ', '	935933'),
        ('鲁A550X3', '	072182'),
        ('鲁A0B793', '	030043'),
        ('鲁A0277G', '	257868'),

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