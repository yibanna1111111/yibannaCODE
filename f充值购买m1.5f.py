oO0 ='''
cron: 0 5 8-22 * * *
new Env('f充值购买');
活动入口微信打开：http://2478987.kej88yj.7lvt1u449.widfx91o0uv0d.cloud/?p=2478987
下载地址：https://www.123pan.com/s/xzeSVv-IHpfv.html
公告地址：http://175.24.153.42:8881/getmsg?type=czgm
使用方法：
1.活动入口,微信打开：http://2478987.kej88yj.7lvt1u449.widfx91o0uv0d.cloud/?p=2478987
'''#line:9
'''
2.打开活动入口，抓包的任意接口cookies中的gfsessionid参数,
3.青龙环境变量菜单，添加本脚本环境变量
名称 ：czgm_config
单个账户参数： ['name|ck|key|uids']
例如：['账号1|729ac1356xxxxb7407bd2ea|keykeykey|uid_xxxxx']
多个账户['name|ck|key|uids','name|ck|key|uids','name|ck|key|uids']
例如：['账号1|729ac1356xxxxb7407bd2ea|keykeykey|uid_xxxxx','账号2|729ac1356xxxxb7407bd2ea|keykeykey|uid_xxxxx','账号3|729ac1356xxxxb7407bd2ea|keykeykey|uid_xxxxx']
参数说明与获取：
ck:打开活动入口，抓包的任意接口cookies中的gfsessionid参数
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
青名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"appToken":"xxxx"}
例如：{"printf":0,"threadingf":1,"appToken":"AT_r1vNXQdfgxxxxxscPyoORYg"}
参数说明：
printf 0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
appToken 这个是填wxpusher的appToken

5.提现标准默认是3000，与需要修改，请在本脚本最下方，按照提示修改

'''#line:37
import threading #line:38
import time #line:39
import hashlib #line:40
import requests #line:41
import random #line:42
import re #line:43
import json #line:44
import os #line:45
checkDict ={'MzkyMzI5NjgxMA==':['每天趣闻事',''],'MzkzMzI5NjQ3MA==':['欢闹青春',''],'Mzg5NTU4MzEyNQ==':['推粉宝助手',''],'Mzg3NzY5Nzg0NQ==':['新鲜事呦',''],'MzU5OTgxNjg1Mg==':['动感比特',''],'Mzg4OTY5Njg4Mw==':['邻居趣事闻','gh_60ba451e6ad7'],'MzI1ODcwNTgzNA==':['麻辣资讯','gh_1df5b5259cba'],'Mzg2NDY5NzU0Mw==':['天天趣闻事','gh_1b3c3773acd0'],"MzA4OTI3ODY4Mg==":['','',''],"MzAwNTIzNjYzNA==":['','',''],"Mzg4NjY5NzE4NQ==":['','',''],"MzkwODI5NzQ4MQ==":['','',''],"MzkzMzI5Njc0Nw==":['','',''],"Mzg5NDg5MDY3Ng==":['','',''],"MzA3MjMwMTYwOA==":['','',''],"MzkyNTM5OTc3OQ==":['','',''],"MjM5OTQ0NzI3Ng==":['','',''],"MzkwOTU3MDI1OA==":['','',''],"MzAwOTc2NDExMA==":['','',''],"MzA3OTI4MDMxMA==":['','',''],"MzkxNzI2ODcwMQ==":['','',''],"MzA3MDMxNzMzOA==":['','',''],"Mzg3NjAwODMwMg==":['','',''],"MzI3NDE2ODk1Nw==":['','',''],"MzIyMDMyNTMwMw==":['','',''],"MzIzMjY2NTMwNQ==":['','',''],"MzkxNzMwMjY5Mg==":['','',''],"MzA5Njg3MDk2Ng==":['','',''],"MzA5MzM1OTY2OQ==":['','',''],"MzA4NTQwNjc3OQ==":['','',''],"MjM5NTY5OTU0MQ==":['','',''],"MzU1NTc4OTg2Mw==":['','',''],"MzkwMzI0NjQ4Mw==":['','',''],"MzI3OTA2NDk0Nw==":['','',''],"MjM5MDU4ODgwMw==":['','',''],"Mzg4NzUyMjQxMw==":['','',''],}#line:84
def getmsg ():#line:86
    OOO00O0O0OO00OO0O ='v1.5f'#line:87
    O00O0OO0O0OO0O00O =''#line:88
    try :#line:89
        O000000O00000OO0O ='http://175.24.153.42:8881/getmsg'#line:90
        OOOOOOO00OO00OOOO ={'type':'czgm'}#line:91
        O00O0OO0O0OO0O00O =requests .get (O000000O00000OO0O ,params =OOOOOOO00OO00OOOO )#line:92
        OOOOO0000O000OOOO =O00O0OO0O0OO0O00O .json ()#line:93
        OO00OO0000OOOOO0O =OOOOO0000O000OOOO .get ('version')#line:94
        O0OOOOOO00O0O0OO0 =OOOOO0000O000OOOO .get ('gdict')#line:95
        OOOO0O0OOO0O000OO =OOOOO0000O000OOOO .get ('gmmsg')#line:96
        print ('系统公告:',OOOO0O0OOO0O000OO )#line:97
        print (f'最新版本{OO00OO0000OOOOO0O}当前版本{OOO00O0O0OO00OO0O}')#line:98
        print (f'系统的公众号字典{len(O0OOOOOO00O0O0OO0)}个:{O0OOOOOO00O0O0OO0}')#line:99
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:100
        OOOO0000OO0O000OO =len (O0OOOOOO00O0O0OO0 )#line:101
        OO00O00OO000OOOO0 =len (checkDict .values ())#line:102
        if OOOO0000OO0O000OO >OO00O00OO000OOOO0 :#line:103
            print (f'新增了{OOOO0000OO0O000OO - OO00O00OO000OOOO0}个过检测字典，快手动去脚本的checkDict里添加吧')#line:104
        print ('='*50 )#line:105
    except Exception as O0OO000OOO0000000 :#line:106
        print (O00O0OO0O0OO0O00O .text )#line:107
        print (O0OO000OOO0000000 )#line:108
        print ('公告服务器异常')#line:109
def push (OO0O0OO00O00000OO ,OOOOO0O00OOO00OO0 ,O00O000OOOO0O00O0 ,O000OO0O0O0OO0OOO ,OOO0OO00O0O00000O ,O0O0OOOOOO0OOOOOO ):#line:112
    OOOOO0O0OO00OOOOO ='''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>TITLE</title>
<style type=text/css>
   body {
   	background-image: linear-gradient(120deg, #fdfbfb 0%, #a5d0e5 100%);
    background-size: 300%;
    animation: bgAnimation 6s linear infinite;
}
@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
</style>
</head>
<body>
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
<p><a href="http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl=LINK">点击阅读检测文章</a></p><br>
</body>
</html>
    '''#line:137
    OO0OOOO0OO0O00O00 =OOOOO0O0OO00OOOOO .replace ('TITTLE',OO0O0OO00O00000OO ).replace ('LINK',OOOOO0O00OOO00OO0 ).replace ('TEXT',O00O000OOOO0O00O0 ).replace ('TYPE',O000OO0O0O0OO0OOO ).replace ('KEY',O0O0OOOOOO0OOOOOO )#line:139
    O000O0OO0000OO00O ={"appToken":appToken ,"content":OO0OOOO0OO0O00O00 ,"summary":OO0O0OO00O00000OO ,"contentType":2 ,"uids":[OOO0OO00O0O00000O ]}#line:146
    OO0O000O000O0OOO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:147
    try :#line:148
        OO00OO0O0OOOO0OOO =requests .post (url =OO0O000O000O0OOO0 ,json =O000O0OO0000OO00O ).text #line:149
        print (OO00OO0O0OOOO0OOO )#line:150
        return True #line:151
    except :#line:152
        print ('推送失败！')#line:153
        return False #line:154
def sha_256 (O00000O0000000O0O ):#line:157
    O0OOOO00O00O00O0O =hashlib .sha256 ()#line:158
    O0OOOO00O00O00O0O .update (O00000O0000000O0O .encode ())#line:159
    OO0OOO0OO0O00O000 =O0OOOO00O00O00O0O .hexdigest ()#line:160
    return OO0OOO0OO0O00O000 #line:161
def getinfo (OO00O0O0OO0OO00OO ):#line:164
    try :#line:165
        OO00OOOOO000000OO =requests .get (OO00O0O0OO0OO00OO )#line:166
        OOOO0OOOOOO00OO00 =re .sub ('\s','',OO00OOOOO000000OO .text )#line:168
        O00OO00OO0000O00O =re .findall ('varbiz="(.*?)"\|\|',OOOO0OOOOOO00OO00 )#line:169
        if O00OO00OO0000O00O !=[]:#line:170
            O00OO00OO0000O00O =O00OO00OO0000O00O [0 ]#line:171
        if O00OO00OO0000O00O ==''or O00OO00OO0000O00O ==[]:#line:172
            if '__biz'in OO00O0O0OO0OO00OO :#line:173
                O00OO00OO0000O00O =re .findall ('__biz=(.*?)&',OO00O0O0OO0OO00OO )#line:174
                if O00OO00OO0000O00O !=[]:#line:175
                    O00OO00OO0000O00O =O00OO00OO0000O00O [0 ]#line:176
        O0OO00O0OOOOOO0OO =re .findall ('varnickname=htmlDecode\("(.*?)"\);',OOOO0OOOOOO00OO00 )#line:177
        if O0OO00O0OOOOOO0OO !=[]:#line:178
            O0OO00O0OOOOOO0OO =O0OO00O0OOOOOO0OO [0 ]#line:179
        OOOO0OOO00OO0OOO0 =re .findall ('varuser_name="(.*?)";',OOOO0OOOOOO00OO00 )#line:180
        if OOOO0OOO00OO0OOO0 !=[]:#line:181
            OOOO0OOO00OO0OOO0 =OOOO0OOO00OO0OOO0 [0 ]#line:182
        O0OOOOOOO0OO0O0O0 =re .findall ("varmsg_title='(.*?)'\.html\(",OOOO0OOOOOO00OO00 )#line:183
        if O0OOOOOOO0OO0O0O0 !=[]:#line:184
            O0OOOOOOO0OO0O0O0 =O0OOOOOOO0OO0O0O0 [0 ]#line:185
        O00O0OO0OO0O000OO =f'公众号唯一标识：{O00OO00OO0000O00O}|文章:{O0OOOOOOO0OO0O0O0}|作者:{O0OO00O0OOOOOO0OO}|账号:{OOOO0OOO00OO0OOO0}'#line:186
        print (O00O0OO0OO0O000OO )#line:187
        return O0OO00O0OOOOOO0OO ,OOOO0OOO00OO0OOO0 ,O0OOOOOOO0OO0O0O0 ,O00O0OO0OO0O000OO ,O00OO00OO0000O00O #line:188
    except Exception as O0O0O0OO000O000O0 :#line:189
        print (O0O0O0OO000O000O0 )#line:190
        print ('异常')#line:191
        return False #line:192
class HHYD ():#line:195
    def __init__ (OO0000O0OO0O0O000 ,OOO0O00OO0OOOOO0O ):#line:196
        print (OOO0O00OO0OOOOO0O )#line:197
        OO0000O0OO0O0O000 .name =OOO0O00OO0OOOOO0O [0 ]#line:198
        OO0000O0OO0O0O000 .ck =OOO0O00OO0OOOOO0O [1 ]#line:199
        OO0000O0OO0O0O000 .key =OOO0O00OO0OOOOO0O [2 ]#line:200
        OO0000O0OO0O0O000 .uids =OOO0O00OO0OOOOO0O [3 ]#line:201
        OO0000O0OO0O0O000 .headers ={'Host':'2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud','Accept':'application/json, text/plain, */*','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'gfsessionid={OO0000O0OO0O0O000.ck}',}#line:209
        OO0000O0OO0O0O000 .sec =requests .session ()#line:210
        OO0000O0OO0O0O000 .sec .headers =OO0000O0OO0O0O000 .headers #line:211
    def printjson (O0O000OO000OOOO0O ,O000O0O0O000OOOOO ):#line:213
        if printf ==0 :#line:214
            return #line:215
        print (O0O000OO000OOOO0O .name ,O000O0O0O000OOOOO )#line:216
    def setstatus (OOO0OOOO000O00OOO ):#line:218
        try :#line:219
            O00000000O00O0O0O ='http://175.24.153.42:8882/setstatus'#line:220
            OO00O0000O0000000 ={'key':OOO0OOOO000O00OOO .key ,'type':'czgm','val':'1','ven':oO0 }#line:221
            OOOOO000O0OO0OO00 =requests .get (O00000000O00O0O0O ,params =OO00O0000O0000000 ,timeout =10 )#line:222
            print (OOO0OOOO000O00OOO .name ,OOOOO000O0OO0OO00 .text )#line:223
            if '无效'in OOOOO000O0OO0OO00 .text :#line:224
                exit (0 )#line:225
        except Exception as O0O00OOO00O000OOO :#line:226
            print ('设置状态异常')#line:227
            print (O0O00OOO00O000OOO )#line:228
    def getstatus (OO0OO0OOOOO0OO0OO ):#line:230
        try :#line:231
            O0OO000000O00000O ='http://175.24.153.42:8882/getstatus'#line:232
            O000O0O00O00O0O0O ={'key':OO0OO0OOOOO0OO0OO .key ,'type':'czgm'}#line:233
            OOO0000000OO0OO0O =requests .get (O0OO000000O00000O ,params =O000O0O00O00O0O0O ,timeout =3 )#line:234
            return OOO0000000OO0OO0O .text #line:235
        except Exception as O0OO000O000OO00O0 :#line:236
            print ('查询状态异常',O0OO000O000OO00O0 )#line:237
            return False #line:238
    def user_info (O00O000OO0000O0OO ):#line:240
        if hashlib .md5 (oO0 .encode ()).hexdigest ()!='1d6cd5931de3b03d1a32518f4d66e7fc':O00O000OO0000O0OO .setstatus ()#line:241
        OO000000OO00OO00O =int (time .time ())#line:242
        OO0O0OOO0OO0OO00O =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OO000000OO00OO00O}'#line:243
        O00O00OO0OOO0O000 =sha_256 (OO0O0OOO0OO0OO00O )#line:244
        OOO0O000000O00OOO =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/user/info?time={OO000000OO00OO00O}&sign={O00O00OO0OOO0O000}'#line:245
        O0O000OO00OO0OOO0 =''#line:246
        try :#line:247
            O0O000OO00OO0OOO0 =O00O000OO0000O0OO .sec .get (OOO0O000000O00OOO )#line:248
            O0OO000O0O0O0O0OO =O0O000OO00OO0OOO0 .json ()#line:249
            if O0OO000O0O0O0O0OO .get ('code')==0 :#line:250
                print (O00O000OO0000O0OO .name ,f'用户UID:{O0OO000O0O0O0O0OO.get("data").get("uid")}')#line:251
                return True #line:252
            else :#line:253
                print (O00O000OO0000O0OO .name ,f'获取用户信息失败，账号异常')#line:254
                return False #line:255
        except :#line:256
            print (O00O000OO0000O0OO .name ,O0O000OO00OO0OOO0 .text )#line:257
            print (O00O000OO0000O0OO .name ,f'获取用户信息失败,gfsessionid无效，请检测gfsessionid是否正确')#line:258
            return False #line:259
    def msg (OO0O0OO000OOOOOO0 ):#line:261
        OOO0OO0O000O00OOO =''#line:262
        try :#line:263
            O0O0O00O0O000OOO0 =int (time .time ())#line:264
            O0OOOO00OOO00OOO0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O0O0O00O0O000OOO0}'#line:265
            O0O0OOO0O00O00OOO =sha_256 (O0OOOO00OOO00OOO0 )#line:266
            OO000O0OO00OO0000 =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/user/msg?time={O0O0O00O0O000OOO0}&sign={O0O0OOO0O00O00OOO}'#line:267
            OOO0OO0O000O00OOO =OO0O0OO000OOOOOO0 .sec .get (OO000O0OO00OO0000 )#line:268
            O00O0O000OOO0O000 =OOO0OO0O000O00OOO .json ()#line:269
            print (OO0O0OO000OOOOOO0 .name ,f'系统公告:{O00O0O000OOO0O000.get("data").get("msg")}')#line:270
        except :#line:271
            print (OO0O0OO000OOOOOO0 .name ,OOO0OO0O000O00OOO .text )#line:272
            return False #line:273
    def read_info (OOO0O0000O000O00O ):#line:275
        O0OO0O0O00O0OO0O0 =''#line:276
        try :#line:277
            OO0000OO0O0OO0O0O =int (time .time ())#line:278
            OOO00O0O0OO00O000 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OO0000OO0O0OO0O0O}'#line:279
            O0000O0O00000000O =sha_256 (OOO00O0O0OO00O000 )#line:280
            O0000O0OO0O0O0O0O =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/read/info?time={OO0000OO0O0OO0O0O}&sign={O0000O0O00000000O}'#line:281
            O0OO0O0O00O0OO0O0 =OOO0O0000O000O00O .sec .get (O0000O0OO0O0O0O0O )#line:282
            O0O0OO0OO0O0OO0OO =O0OO0O0O00O0OO0O0 .json ()#line:283
            OOO0O0000O000O00O .remain =O0O0OO0OO0O0OO0OO .get ("data").get ("remain")#line:284
            print (OOO0O0000O000O00O .name ,f'今日已经阅读了{O0O0OO0OO0O0OO0OO.get("data").get("read")}篇文章，今日总金币{O0O0OO0OO0O0OO0OO.get("data").get("gold")}，剩余{OOO0O0000O000O00O.remain}')#line:286
        except :#line:287
            print (OOO0O0000O000O00O .name ,O0OO0O0O00O0OO0O0 .text )#line:288
            return False #line:289
    def read (O0000OO00O0000O0O ):#line:291
        print (O0000OO00O0000O0O .name ,'阅读开始')#line:292
        while True :#line:293
            print (O0000OO00O0000O0O .name ,'-'*50 )#line:294
            OOO0OO00O0O00OO00 =int (time .time ())#line:295
            OO00OOOOO00O0OO00 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OOO0OO00O0O00OO00}'#line:296
            OOO0O0O0OOOOO0OO0 =sha_256 (OO00OOOOO00O0OO00 )#line:297
            OOOOO00O0O00O000O =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/read/task?time={OOO0OO00O0O00OO00}&sign={OOO0O0O0OOOOO0OO0}'#line:298
            O0OOOO000O000OO0O =O0000OO00O0000O0O .sec .get (OOOOO00O0O00O000O )#line:299
            O0000OO00O0000O0O .printjson (O0OOOO000O000OO0O .text )#line:300
            O0O0000OO0O00000O =O0OOOO000O000OO0O .json ()#line:301
            O0O0O0O0OO0000OO0 =O0O0000OO0O00000O .get ('code')#line:302
            if O0O0O0O0OO0000OO0 ==0 :#line:303
                O000O00O00OO00000 =O0O0000OO0O00000O .get ('data').get ('link')#line:304
                print (O0000OO00O0000O0O .name ,'获取到阅读链接成功')#line:305
                O000OO000OO000O0O =O000O00O00OO00000 .encode ().decode ()#line:306
                if 'weixin.'not in O000OO000OO000O0O :#line:307
                    O0O0O00OOO000OOOO =O0000OO00O0000O0O .getWxurl (O000OO000OO000O0O )#line:308
                else :#line:309
                    O0O0O00OOO000OOOO =O000OO000OO000O0O #line:310
                OO00000OO00O00O00 =getinfo (O0O0O00OOO000OOOO )#line:311
                if O0000OO00O0000O0O .testCheck (OO00000OO00O00O00 ,O0O0O00OOO000OOOO )==False :#line:312
                    return False #line:313
                O00O000O0OOOOOO00 =random .randint (7 ,10 )#line:314
                print (O0000OO00O0000O0O .name ,'本次模拟阅读',O00O000O0OOOOOO00 ,'秒')#line:315
                time .sleep (O00O000O0OOOOOO00 )#line:316
            elif O0O0O0O0OO0000OO0 ==400 :#line:317
                print (O0000OO00O0000O0O .name ,'未知情况400')#line:318
                time .sleep (10 )#line:319
                continue #line:320
            elif O0O0O0O0OO0000OO0 ==20001 :#line:321
                print (O0000OO00O0000O0O .name ,'未知情况20001')#line:322
            else :#line:323
                print (O0000OO00O0000O0O .name ,O0O0000OO0O00000O .get ('message'))#line:324
                return False #line:325
            O0000OO00O0000O0O .msg ()#line:327
            OOO0OO00O0O00OO00 =int (time .time ())#line:328
            OO0OO0OOO0OOOOOO0 =O0000OO00O0000O0O .sec .headers .copy ()#line:329
            OO0OO0OOO0OOOOOO0 .update ({'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Origin':'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud'})#line:331
            OO00OOOOO00O0OO00 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={OOO0OO00O0O00OO00}'#line:332
            OOO0O0O0OOOOO0OO0 =sha_256 (OO00OOOOO00O0OO00 )#line:333
            O00OO00OO0OO000O0 =f'time={OOO0OO00O0O00OO00}&sign={OOO0O0O0OOOOO0OO0}'#line:334
            OOOOO00O0O00O000O =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/read/finish'#line:335
            O0OOOO000O000OO0O =requests .post (OOOOO00O0O00O000O ,headers =OO0OO0OOO0OOOOOO0 ,data =O00OO00OO0OO000O0 )#line:336
            O0000OO00O0000O0O .printjson (O0OOOO000O000OO0O .text )#line:337
            O0O0000OO0O00000O =O0OOOO000O000OO0O .json ()#line:338
            if O0O0000OO0O00000O .get ('code')==0 :#line:339
                if O0O0000OO0O00000O .get ('data').get ('check')==False :#line:340
                    OO0OO0O00000OOO00 =O0O0000OO0O00000O .get ('data').get ('gain')#line:341
                    O0000OO00O0000O0O .remain =O0O0000OO0O00000O .get ("data").get ("remain")#line:342
                    print (O0000OO00O0000O0O .name ,f"阅读文章成功获得{OO0OO0O00000OOO00}金币")#line:343
                    print (O0000OO00O0000O0O .name ,f'当前已经阅读了{O0O0000OO0O00000O.get("data").get("read")}篇文章，今日总金币{O0O0000OO0O00000O.get("data").get("gold")}，剩余{O0000OO00O0000O0O.remain}')#line:345
                else :#line:346
                    print (O0000OO00O0000O0O .name ,"过检测成功")#line:347
                    print (O0000OO00O0000O0O .name ,f'当前已经阅读了{O0O0000OO0O00000O.get("data").get("read")}篇文章，今日总金币{O0O0000OO0O00000O.get("data").get("gold")}，剩余{O0000OO00O0000O0O.remain}')#line:349
            else :#line:350
                return False #line:351
            time .sleep (1 )#line:352
            print (O0000OO00O0000O0O .name ,'开始本次阅读')#line:353
    def withdraw (O0OO000O00O0OO00O ):#line:355
        if O0OO000O00O0OO00O .remain <txbz :#line:356
            print (O0OO000O00O0OO00O .name ,'没有达到提现标准')#line:357
            return False #line:358
        O00OO0OO000OOO00O =int (time .time ())#line:359
        OO00OO0O0O00O0OO0 =f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={O00OO0OO000OOO00O}'#line:360
        OOOO00OOOOO00OO0O =sha_256 (OO00OO0O0O00O0OO0 )#line:361
        OO000OOOO0OOOO0OO =f'http://2478987.txpffkrowsu.tewn8sas1mh369.2ba6s0fq21.cloud/withdraw/wechat?time={O00OO0OO000OOO00O}&sign={OOOO00OOOOO00OO0O}'#line:362
        OOOO00OOOO00OO0O0 =O0OO000O00O0OO00O .sec .get (OO000OOOO0OOOO0OO ,headers =O0OO000O00O0OO00O .headers )#line:363
        print (O0OO000O00O0OO00O .name ,'提现结果',OOOO00OOOO00OO0O0 .text )#line:364
    def getWxurl (O0OO0OO00OOOO0O00 ,OOOOO00000O00OOO0 ):#line:365
        OOOOOOO0OOO0O00OO =requests .get (OOOOO00000O00OOO0 ,headers =O0OO0OO00OOOO0O00 .headers ,allow_redirects =False )#line:366
        return OOOOOOO0OOO0O00OO .headers .get ('Location')#line:367
    def testCheck (O00O0OOOOO0000O0O ,OO0OO00OO00OO00O0 ,O00OOO0OO0O0O0O00 ):#line:368
        if checkDict .get (OO0OO00OO00OO00O0 [4 ])!=None :#line:369
            O00O0OOOOO0000O0O .setstatus ()#line:370
            for OO0O00OO0O00O0OO0 in range (60 ):#line:371
                if OO0O00OO0O00O0OO0 %30 ==0 :#line:372
                    push (f'{O00O0OOOOO0000O0O.name}:充值购买过检测',O00OOO0OO0O0O0O00 ,OO0OO00OO00OO00O0 [3 ],'czgm',O00O0OOOOO0000O0O .uids ,O00O0OOOOO0000O0O .key )#line:373
                OO0OOOOO00OOOO0O0 =O00O0OOOOO0000O0O .getstatus ()#line:374
                if OO0OOOOO00OOOO0O0 =='0':#line:375
                    print (O00O0OOOOO0000O0O .name ,'过检测文章已经阅读')#line:376
                    return True #line:377
                elif OO0OOOOO00OOOO0O0 =='1':#line:378
                    print (O00O0OOOOO0000O0O .name ,f'正在等待过检测文章阅读结果{OO0O00OO0O00O0OO0}秒。。。')#line:379
                    time .sleep (1 )#line:380
                else :#line:381
                    print (O00O0OOOOO0000O0O .name ,f'回调服务器请求超时，等待中{OO0O00OO0O00O0OO0}秒。。。')#line:382
                    time .sleep (1 )#line:383
            print (O00O0OOOOO0000O0O .name ,'过检测超时中止脚本防止黑号')#line:384
            return False #line:385
        else :#line:386
            return True #line:387
    def run (O00OO0OOO0000O00O ):#line:388
        O00OO0OOO0000O00O .user_info ()#line:389
        O00OO0OOO0000O00O .msg ()#line:390
        O00OO0OOO0000O00O .read_info ()#line:391
        O00OO0OOO0000O00O .read ()#line:392
        time .sleep (5 )#line:393
        O00OO0OOO0000O00O .withdraw ()#line:394
if __name__ =='__main__':#line:397
    pushconfig =os .getenv ('push_config')#line:398
    if pushconfig ==None :#line:399
        print ('请检查你的推送变量名称是否填写')#line:400
        exit (0 )#line:401
    try :#line:402
        pushconfig =json .loads (pushconfig .replace ("'",'"'))#line:403
    except Exception as e :#line:404
        print (e )#line:405
        print ('你填写的是：',pushconfig )#line:406
        print ('请检查你的推送变量参数是否填写正确')#line:407
        exit (0 )#line:408
    czgmconfig =os .getenv ('czgm_config')#line:409
    if czgmconfig ==None :#line:410
        print ('请检查你的充值购买脚本变量名称是否填写')#line:411
        exit (0 )#line:412
    try :#line:413
        czgmconfig =json .loads (czgmconfig .replace ("'",'"'))#line:414
    except Exception as e :#line:415
        print (e )#line:416
        print ('你填写的是：',czgmconfig )#line:417
        print ('请检查你的充值购买脚本变量参数是否填写正确')#line:418
        exit (0 )#line:419
    printf =pushconfig ['printf']#line:420
    appToken =pushconfig ['appToken']#line:421
    threadingf =pushconfig ['threadingf']#line:422
    getmsg ()#line:423
    txbz =3000 #line:424
    tl =[]#line:425
    if threadingf ==1 :#line:426
        for i in czgmconfig :#line:427
            cg =i .split ('|')#line:428
            print ('*'*50 )#line:429
            print (f'开始执行{i[0]}')#line:430
            api =HHYD (cg )#line:431
            t =threading .Thread (target =api .run ,args =())#line:432
            tl .append (t )#line:433
            t .start ()#line:434
            time .sleep (0.5 )#line:435
        for t in tl :#line:436
            t .join ()#line:437
    elif threadingf ==0 :#line:438
        for i in czgmconfig :#line:439
            cg =i .split ('|')#line:440
            print ('*'*50 )#line:441
            print (f'开始执行{cg[0]}')#line:442
            api =HHYD (cg )#line:443
            api .run ()#line:444
            print (f'{cg[0]}执行完毕')#line:445
            time .sleep (3 )#line:446
    else :#line:447
        print ('请确定推送变量中threadingf参数是否正确')#line:448
    print ('全部账号执行完成')#line:449
