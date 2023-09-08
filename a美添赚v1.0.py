import time
import requests
import random
import JhWxPusher
import getWxInfo
import config
import threading
checkDict={
'MzkzNjI3NDAwOA==':['木新领袋管家','gh_04e096463e91'],
}
def getmsg():
    lvsion = 'v1.0_a'
    r=''
    try:
        u='http://175.24.153.42:8881/getmsg'
        p={'type':'mtzyd'}
        r=requests.get(u,params=p)
        rj=r.json()
        version=rj.get('version')
        gdict = rj.get('gdict')
        gmmsg = rj.get('gmmsg')
        print('系统公告:',gmmsg)
        print(f'最新版本{version},当前版本{lvsion}')
        print(f'系统的公众号字典{len(gdict)}个:{gdict}')
        print(f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')
        print('='*50)
    except Exception as e:
        print(r.text)
        print(e)
        print('公告服务器异常')

class MTZYD():
    def __init__(self,cg):
        self.cg=cg
        self.key=cg['key']
        self.name=cg['name']
        self.headers={
            'Authorization': cg['ck'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'content-type': 'application/json',
            'Accept': '*/*',
            'Origin': 'http://71692693186.tt.bendishenghuochwl1.cn',
            'Referer': 'http://71692693186.tt.bendishenghuochwl1.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
        }

    def printjson(self,text):
        if printf == 0:
            return
        print(self.name,text)

    def setstatus(self):
        try:
            u = 'http://175.24.153.42:8882/setstatus'
            p = {'key': self.key, 'type': 'mtzyd', 'val': '1'}
            r = requests.get(u, params=p,timeout=10)
            print(self.name, r.text)
        except Exception as e:
            print('设置状态异常')
            print(e)

    def getstatus(self):
        try:
            u = 'http://175.24.153.42:8882/getstatus'
            p = {'key': self.key, 'type': 'mtzyd'}
            r = requests.get(u, params=p,timeout=3)
            return r.text
        except Exception as e:
            print('查询状态异常',e)
            return False
    def user_info(self):
        u='http://api.mengmorwpt1.cn/h5_share/user/info'
        r=requests.post(u,headers=self.headers,json={"openid":0})
        self.printjson(r.text)
        rj=r.json()
        if rj.get('code')==200:
            nickname=rj.get('data').get('nickname')
            points=rj.get('data').get('points')
            used_points = rj.get('data').get('used_points')
            self.sy=points-used_points
            print(self.name,f'当前账号：{nickname},总积分积分：{points}，已经提现：{used_points},剩余：{self.sy}')
        else:
            print(self.name,'获取账号信息异常,ck可能失效请重新获取')
            return False
    def sign(self):
        u='http://api.mengmorwpt1.cn/h5_share/user/sign'
        r = requests.post(u, headers=self.headers, json={"openid": 0})
        self.printjson(r.text)
        print(self.name,'签到成功')
    def getMissions(self):
        ''
        u='http://api.mengmorwpt1.cn/h5_share/daily/getMissions'
        r = requests.post(u, headers=self.headers, json={"openid": 0})
        rj = r.json()
        if rj.get('code')!=200:
            self.printjson(r.text)
            return False
        info=''
        for i in rj.get('data'):
            if i.get('title')=='文章阅读推荐':
                info=i
                break
        if info=='':
            self.printjson(r.text)
            print(self.name,'没有找到任务')
            return False
        self.printjson(info)
        if info.get('left_time')=='开始活动':
            return True
        else:
            print(self.name,'下次阅读,',end='')
            print(self.name,info.get('left_time'))
            return False
    def read_info(self):
        u=f'http://api.mengmorwpt1.cn/h5_share/daily/get_read'
        r = requests.post(u, headers=self.headers, json={"openid": 0})
        self.printjson(r.text)
        rj = r.json()
        if rj.get('code')==200:
            self.link=rj.get('data').get('link')
        else:
            print(self.name,'获取阅读链接异常异常')
            return False
    def gettaskinfo(self,infolist):
        for i in infolist:
            if i.get('url'):
                return i
    def read(self):
        print(self.name,'阅读开始')
        h={
            'Host': 'api.wanjd.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'http://uha294070.294070nwq.com.294070u.meitianzhuan2.cn',
            'Referer': 'http://uha294070.294070nwq.com.294070u.meitianzhuan2.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh',
        }
        self.num=1000
        pt=0
        while True:
            print(self.name,'-'*50)
            u1='https://api.wanjd.cn/wxread/articles/tasks'
            p={'href':self.link}
            r=requests.post(u1,headers=h,data=p)
            self.printjson(r.text)
            rj = r.json()
            code=rj.get('code')
            if code==500:
                print(self.name,'阅读异常')
                print(self.name,rj.get('data'))
                break
            if code==200:
                if pt==0:
                    self.num= len(rj.get('data'))
                    pt=1
                taskinfo=self.gettaskinfo(rj.get('data'))
                url=taskinfo.get('url')
                id=taskinfo.get('id')
                a = getWxInfo.getinfo(url)
                if self.testCheck(a, url) == False:
                    return False
                tsm = random.randint(7, 10)
                print(self.name,f'本次模拟读{tsm}秒')
                time.sleep(tsm)
                u1 = 'https://api.wanjd.cn/wxread/articles/three_read'
                p1 = {'id': id, 'href': self.link}
                r = requests.post(u1, headers=h, data=p1)
                self.printjson(r.text)
                if self.num <= 0:
                    break
                self.num-=1
        curl = 'https://api.wanjd.cn/wxread/articles/check_success'
        cp = {'type': 1, 'href': self.link}
        cr = requests.post(curl, headers=h, data=cp)
        self.printjson(cr.text)
        print(self.name,'本次阅读已完成')
    def testCheck(self, a, link):
        if a[4]==[]:
            print(self.name,'这个链接没有获取到微信号id',link)
            return True
        if checkDict.get(a[4]) != None:
            self.setstatus()
            for i in range(60):
                if i % 30 == 0:
                    JhWxPusher.push(self.cg['name'], link, a[3], 'mtzyd',self.cg['uids'],self.key)
                getstatusinfo = self.getstatus()
                if getstatusinfo == '0':
                    print(self.name,'过检测文章已经阅读')
                    return True
                elif getstatusinfo == '1':
                    print(self.name,f'正在等待过检测文章阅读结果{i}秒。。。')
                    time.sleep(1)
                else:
                    print(self.name, f'回调服务器请求超时，等待中{i}秒。。。')
                    time.sleep(1)
            print(self.name,'过检测超时中止脚本防止黑号')
            return False
        else:
            return True
    def withdraw(self):
        if self.sy<1000:
            print(self.name,'没有达到提现标准')
            return False
        u='http://api.mengmorwpt1.cn/h5_share/user/withdraw'
        r=requests.post(u,headers=self.headers)
        print(self.name,'提现结果',r.text)
    def run(self):
        if self.user_info()==False:
            return False
        self.sign()
        if self.getMissions():
            self.read_info()
            self.read()
            self.user_info()
        self.withdraw()
if __name__ == '__main__':
    printf = config.printf
    getmsg()
    tl=[]
    if config.threadingf == 1:
        for i in config.mtzconfig:
            print('*' * 50)
            print(f'开始执行{i["name"]}')
            api = MTZYD(i)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            time.sleep(0.5)
        for t in tl:
            t.join()
    elif config.threadingf == 0:
        for i in config.mtzconfig:
            print('*' * 50)
            print(f'开始执行{i["name"]}')
            api = MTZYD(i)
            api.run()
            print(f'{i["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定config配置文件中threadingf参数是否正确')
    print('全部账号执行完成')