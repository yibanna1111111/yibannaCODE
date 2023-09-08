import config
import time
import hashlib
import requests
import random
import getWxInfo
import JhWxPusher
import threading
checkDict = {
    'MzkyMzI5NjgxMA==': ['每天趣闻事', ''],
    'MzkzMzI5NjQ3MA==': ['欢闹青春', ''],
    'Mzg5NTU4MzEyNQ==': ['推粉宝助手', ''],
    'Mzg3NzY5Nzg0NQ==': ['新鲜事呦', ''],
    'MzU5OTgxNjg1Mg==': ['动感比特', ''],
    'Mzg4OTY5Njg4Mw==': ['邻居趣事闻', 'gh_60ba451e6ad7'],
    'MzI1ODcwNTgzNA==': ['麻辣资讯', 'gh_1df5b5259cba'],
}
def getmsg():
    lvsion = 'v1.1_a'
    r=''
    try:
        u='http://175.24.153.42:8881/getmsg'
        p={'type':'czgm'}
        r=requests.get(u,params=p)
        rj=r.json()
        version=rj.get('version')
        gdict = rj.get('gdict')
        gmmsg = rj.get('gmmsg')
        print('系统公告:',gmmsg)
        print(f'最新版本{version}当前版本{lvsion}')
        print(f'系统的公众号字典{len(gdict)}个:{gdict}')
        print(f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')
        print('='*50)
    except Exception as e:
        print(r.text)
        print(e)
        print('公告服务器异常')

def sha_256(text):
    hash = hashlib.sha256()
    hash.update(text.encode())
    t = hash.hexdigest()
    return t
class HHYD():
    def __init__(self, cg):
        self.cg=cg
        self.key=cg.get('key')
        self.name = cg.get('name')
        self.headers = {
            'Host': '2478987.jilixczlz.ix47965in5.cloud',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh',
            'Cookie': f'gfsessionid={cg["ck"]}',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers

    def setstatus(self):
        try:
            u = 'http://175.24.153.42:8882/setstatus'
            p = {'key': self.key, 'type': 'czgm', 'val': '1'}
            r = requests.get(u, params=p,timeout=10)
            print(self.name, r.text)
        except Exception as e:
            print('设置状态异常')
            print(e)

    def getstatus(self):
        try:
            u = 'http://175.24.153.42:8882/getstatus'
            p = {'key': self.key, 'type': 'czgm'}
            r = requests.get(u, params=p,timeout=3)
            return r.text
        except Exception as e:
            print('查询状态异常',e)
            return False

    def printjson(self, text):
        if printf == 0:
            return
        print(self.name, text)
    def user_info(self):
        ts = int(time.time())
        text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
        sign = sha_256(text)
        u = f'http://2478987.jilixczlz.ix47965in5.cloud/user/info?time={ts}&sign={sign}'
        r = ''
        try:
            r = self.sec.get(u)
            rj = r.json()
            if rj.get('code') == 0:
                print(self.name,f'用户UID:{rj.get("data").get("uid")}')
                return True
            else:
                print(self.name,f'获取用户信息失败，账号异常，请检查你的ck')
                return False
        except:
            print(self.name,f'获取用户信息失败，账号异常，请检查你的ck')
            return False

    def msg(self):
        r = ''
        try:
            ts = int(time.time())
            text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
            sign = sha_256(text)
            u = f'http://2478987.jilixczlz.ix47965in5.cloud/user/msg?time={ts}&sign={sign}'
            r = self.sec.get(u)
            rj = r.json()
            print(self.name,f'系统公告:{rj.get("data").get("msg")}')
        except:
            print(self.name,r.text)
            return False

    def read_info(self):
        r = ''
        try:
            ts = int(time.time())
            text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
            sign = sha_256(text)
            u = f'http://2478987.jilixczlz.ix47965in5.cloud/read/info?time={ts}&sign={sign}'
            r = self.sec.get(u)
            rj = r.json()
            self.remain = rj.get("data").get("remain")
            print(self.name,f'今日已经阅读了{rj.get("data").get("read")}篇文章，今日总金币{rj.get("data").get("gold")}，剩余{self.remain}')
        except:
            print(self.name,r.text)
            return False

    def read(self):
        print(self.name,'阅读开始')
        while True:
            print(self.name,'-' * 50)
            ts = int(time.time())
            text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
            sign = sha_256(text)
            u = f'http://2478987.jilixczlz.ix47965in5.cloud/read/task?time={ts}&sign={sign}'
            r = self.sec.get(u)
            self.printjson(r.text)
            rj = r.json()
            code = rj.get('code')
            if code == 0:
                uncode_link = rj.get('data').get('link')
                print(self.name,'获取到阅读链接成功')
                link = uncode_link.encode().decode()
                a = getWxInfo.getinfo(link)
                if self.testCheck(a, link) == False:
                    return False
                sleeptime = random.randint(7, 10)
                print(self.name,'本次模拟阅读', sleeptime, '秒')
                time.sleep(sleeptime)
            elif code == 400:
                print(self.name,'未知情况400')
                time.sleep(10)
                continue
            elif code == 20001:
                print(self.name,'未知情况20001')
            else:
                print(self.name,rj.get('message'))
                return False
            # -----------------------------
            self.msg()
            ts = int(time.time())
            finish_headers = self.sec.headers.copy()
            finish_headers.update({'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                                   'Origin': 'http://2478987.jilixczlz.ix47965in5.cloud'})
            text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
            sign = sha_256(text)
            p = f'time={ts}&sign={sign}'
            u = f'http://2478987.jilixczlz.ix47965in5.cloud/read/finish'
            r = requests.post(u, headers=finish_headers, data=p)
            self.printjson(r.text)
            rj = r.json()
            if rj.get('code') == 0:
                if rj.get('data').get('check') == False:
                    gain = rj.get('data').get('gain')
                    self.remain = rj.get("data").get("remain")
                    print(self.name,f"阅读文章成功获得{gain}金币")
                    print(self.name,
                        f'当前已经阅读了{rj.get("data").get("read")}篇文章，今日总金币{rj.get("data").get("gold")}，剩余{self.remain}')
                else:
                    print(self.name,"过检测成功")
                    print(self.name,f'当前已经阅读了{rj.get("data").get("read")}篇文章，今日总金币{rj.get("data").get("gold")}，剩余{self.remain}')
            else:
                return False
            time.sleep(1)
            print(self.name,'开始本次阅读')

    def testCheck(self, a, link):
        if checkDict.get(a[4]) != None:
            self.setstatus()
            for i in range(60):
                if i % 30 == 0:
                    JhWxPusher.push(self.cg['name'], link, a[3], 'czgm',self.cg['uids'],self.key)
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
        if self.remain < 10000:
            print(self.name,'没有达到提前标准')
            return False
        ts = int(time.time())
        text = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={ts}'
        sign = sha_256(text)
        u = f'http://2478987.84.8agakd6cqn.cloud/withdraw/wechat?time={ts}&sign={sign}'
        r = self.sec.get(u, headers=self.headers)
        print(self.name,'提现结果', r.text)

    def run(self):
        if self.user_info():
            self.msg()
            self.read_info()
            self.read()
            time.sleep(5)
            self.withdraw()

if __name__ == '__main__':
    printf = config.printf
    getmsg()
    tl=[]
    if config.threadingf == 1:
        for i in config.czgmconfig:
            print('*' * 50)
            print(f'开始执行{i["name"]}')
            api = HHYD(i)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            time.sleep(0.5)
        for t in tl:
            t.join()
    elif config.threadingf == 0:
        for i in config.czgmconfig:
            print('*' * 50)
            print(f'开始执行{i["name"]}')
            api = HHYD(i)
            api.run()
            print(f'{i["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定config配置文件中threadingf参数是否正确')
    print('全部账号执行完成')
