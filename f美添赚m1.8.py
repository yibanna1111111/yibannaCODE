oo0o ='''
cron: 30 */30 8-22 * * *
new Env('f美添赚');
活动入口：http://mtz-1697607152777-1321239794.cos-website.ap-nanjing.tencentcos.cn/pages/app/daily/daily?user_id=115772
下载地址：https://www.123pan.com/s/xzeSVv-IHpfv.html
公告地址：http://175.24.153.42:8881/getmsg?type=mtzyd
使用方法：
1.入口,WX打开：http://mtz-1697607152777-1321239794.cos-website.ap-nanjing.tencentcos.cn/pages/app/daily/daily?user_id=115772
'''#line:9
'''
2.打开活动入口，抓包的任意接口headers中的Authorization参数

3.青龙环境变量菜单或者配置文件，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
青龙添加环境变量名称 ：mtzconfig
方式一：青龙添加环境变量参数 ：
单账户：[{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'}]
多账户：[{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'},{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'}]

方式二：配置文件添加
单账户：export mtzconfig="[{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'}]"
多账户：export mtzconfig="[
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'},
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'},
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'}
]"
参数说明：
name:备注名随意填写
Authorization:打开活动入口，抓包的任意接口headers中的Authorization参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
方式一：青龙添加环境变量参数 ：
名称 ：push_config
参数 ：{"printf":0,"threadingf":1,"appToken":"xxxx"}
方式二：配置文件添加
export push_config="{'printf':'0','threadingf':'1','appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
appToken 这个是填wxpusher的appToken,找不到自己百度
4.本地电脑python运行
在本脚本最下方代码if __name__ == '__main__':下填写
例如
loc_push_config={"printf":0,"threadingf":1,"appToken":"xxxx"}
loc_mtzconfig=[
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'},
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'},
{'name':'备注名','Authorization': 'share:login:729ac13xxxxdb7407bd2ea','key':'xxxxx','uids':'xxxxx'}
]
5.提现标准默认是
定时运行每半个小时一次
'''#line:57
import json #line:58
import time #line:59
import requests #line:60
import random #line:61
import threading #line:62
import re #line:63
import hashlib #line:64
import os #line:65
from urllib .parse import unquote ,quote ,urlparse ,parse_qs #line:66
checkDict ={'oneischeck':['第一篇文章','过检测'],'MzkzNjI3NDAwOA==':['木新领袋管家','gh_04e096463e91'],}#line:70
def getmsg ():#line:71
    O0000O000OO00O00O ='v1.8f'#line:72
    OO0000000OOOO00OO =''#line:73
    try :#line:74
        O0OOOO0OOO0000O0O ='http://175.24.153.42:8881/getmsg'#line:75
        O00O000000O0O00O0 ={'type':'mtzyd'}#line:76
        OO0000000OOOO00OO =requests .get (O0OOOO0OOO0000O0O ,params =O00O000000O0O00O0 )#line:77
        OO0O0OO00OOO0OOOO =OO0000000OOOO00OO .json ()#line:78
        OOOO00O0OOOO0O0OO =OO0O0OO00OOO0OOOO .get ('version')#line:79
        OO0000O0OOOO000OO =OO0O0OO00OOO0OOOO .get ('gdict')#line:80
        O0000O0OO0OOO0OOO =OO0O0OO00OOO0OOOO .get ('gmmsg')#line:81
        print ('系统公告:',O0000O0OO0OOO0OOO )#line:82
        print (f'最新版本{OOOO00O0OOOO0O0OO},当前版本{O0000O000OO00O00O}')#line:83
        print (f'系统的公众号字典{len(OO0000O0OOOO000OO)}个:{OO0000O0OOOO000OO}')#line:84
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:85
        print ('='*50 )#line:86
    except Exception as O0000O0O0OO00000O :#line:87
        print (OO0000000OOOO00OO .text )#line:88
        print (O0000O0O0OO00000O )#line:89
        print ('公告服务器异常')#line:90
def push (O0O00OO00O0OOOO0O ,O0OO0OOOOO00O0O0O ,OO0OOO000OO0O000O ,O00OO0O0O0O0O0OOO ,O000OO0O000O0OO00 ,OO0OOO0OOOOOOO0O0 ):#line:91
    O0OOO0OOOOOOOO0O0 ='''<!DOCTYPE html>
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
    '''#line:116
    OOO0O00OOOO000OO0 =O0OOO0OOOOOOOO0O0 .replace ('TITTLE',O0O00OO00O0OOOO0O ).replace ('LINK',O0OO0OOOOO00O0O0O ).replace ('TEXT',OO0OOO000OO0O000O ).replace ('TYPE',O00OO0O0O0O0O0OOO ).replace ('KEY',OO0OOO0OOOOOOO0O0 )#line:118
    OOO0O0O0O0OO00OOO ={"appToken":appToken ,"content":OOO0O00OOOO000OO0 ,"summary":O0O00OO00O0OOOO0O ,"contentType":2 ,"uids":[O000OO0O000O0OO00 ]}#line:125
    O0OOOO00O00OO0OOO ='http://wxpusher.zjiecode.com/api/send/message'#line:126
    try :#line:127
        OO0000000O00OO0O0 =requests .post (url =O0OOOO00O00OO0OOO ,json =OOO0O0O0O0OO00OOO ).text #line:128
        print (OO0000000O00OO0O0 )#line:129
        return True #line:130
    except :#line:131
        print ('推送失败！')#line:132
        return False #line:133
def getinfo (O00OO00OO00O0OOOO ):#line:135
    try :#line:136
        O00OO0OOOOO0OOO00 =requests .get (O00OO00OO00O0OOOO )#line:137
        O00OOOO0O0O000O0O =re .sub ('\s','',O00OO0OOOOO0OOO00 .text )#line:139
        O0OOO0000O0O0O000 =re .findall ('varbiz="(.*?)"\|\|',O00OOOO0O0O000O0O )#line:140
        if O0OOO0000O0O0O000 !=[]:#line:141
            O0OOO0000O0O0O000 =O0OOO0000O0O0O000 [0 ]#line:142
        if O0OOO0000O0O0O000 ==''or O0OOO0000O0O0O000 ==[]:#line:143
            if '__biz'in O00OO00OO00O0OOOO :#line:144
                O0OOO0000O0O0O000 =re .findall ('__biz=(.*?)&',O00OO00OO00O0OOOO )#line:145
                if O0OOO0000O0O0O000 !=[]:#line:146
                    O0OOO0000O0O0O000 =O0OOO0000O0O0O000 [0 ]#line:147
        O0OO0OO00OO0O0OO0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O00OOOO0O0O000O0O )#line:148
        if O0OO0OO00OO0O0OO0 !=[]:#line:149
            O0OO0OO00OO0O0OO0 =O0OO0OO00OO0O0OO0 [0 ]#line:150
        OOO00OOO0OO0O0OO0 =re .findall ('varuser_name="(.*?)";',O00OOOO0O0O000O0O )#line:151
        if OOO00OOO0OO0O0OO0 !=[]:#line:152
            OOO00OOO0OO0O0OO0 =OOO00OOO0OO0O0OO0 [0 ]#line:153
        OOO0OO0OO0O0OOO0O =re .findall ("varmsg_title='(.*?)'\.html\(",O00OOOO0O0O000O0O )#line:154
        if OOO0OO0OO0O0OOO0O !=[]:#line:155
            OOO0OO0OO0O0OOO0O =OOO0OO0OO0O0OOO0O [0 ]#line:156
        O00O000O0000O000O =f'公众号唯一标识：{O0OOO0000O0O0O000}|文章:{OOO0OO0OO0O0OOO0O}|作者:{O0OO0OO00OO0O0OO0}|账号:{OOO00OOO0OO0O0OO0}'#line:157
        print (O00O000O0000O000O )#line:158
        return O0OO0OO00OO0O0OO0 ,OOO00OOO0OO0O0OO0 ,OOO0OO0OO0O0OOO0O ,O00O000O0000O000O ,O0OOO0000O0O0O000 #line:159
    except Exception as OOO0O00OOO000O000 :#line:160
        print (OOO0O00OOO000O000 )#line:161
        print ('异常')#line:162
        return False #line:163
class MTZYD ():#line:164
    def __init__ (OOOOOOOO0OO0OO00O ,O0000O00OO00OO0OO ):#line:165
        OOOOOOOO0OO0OO00O .name =O0000O00OO00OO0OO ['name']#line:166
        OOOOOOOO0OO0OO00O .key =O0000O00OO00OO0OO ['key']#line:167
        OOOOOOOO0OO0OO00O .uids =O0000O00OO00OO0OO ['uids']#line:168
        OOOOOOOO0OO0OO00O .headers ={'Authorization':O0000O00OO00OO0OO ['Authorization'],'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','content-type':'application/json','Accept':'*/*','Origin':'http://21699521383.tt.bendishenghuochwl1.cn','Referer':'http://21699521383.tt.bendishenghuochwl1.cn/','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh',}#line:178
    def printjson (O00O00O0OOO0O000O ,OOOO0O0OOO0O00O00 ):#line:179
        if printf ==0 :#line:180
            return #line:181
        print (O00O00O0OOO0O000O .name ,OOOO0O0OOO0O00O00 )#line:182
    def setstatus (O000OO0OOOOO0O0O0 ):#line:183
        try :#line:184
            O000OO00OOO00000O ='http://175.24.153.42:8882/setstatus'#line:185
            OOO0000000OO0O0O0 ={'key':O000OO0OOOOO0O0O0 .key ,'type':'mtzyd','val':'1','ven':oo0o }#line:186
            OO0O00OO0O00OO00O =requests .get (O000OO00OOO00000O ,params =OOO0000000OO0O0O0 ,timeout =10 )#line:187
            print (O000OO0OOOOO0O0O0 .name ,OO0O00OO0O00OO00O .text )#line:188
            if '无效'in OO0O00OO0O00OO00O .text :#line:189
                exit (0 )#line:190
        except Exception as OO0000000OOOO0OOO :#line:191
            print (O000OO0OOOOO0O0O0 .name ,'设置状态异常')#line:192
            print (O000OO0OOOOO0O0O0 .name ,OO0000000OOOO0OOO )#line:193
    def getstatus (O00000O00O0000O00 ):#line:195
        try :#line:196
            O0000O0O0O0OO0O0O ='http://175.24.153.42:8882/getstatus'#line:197
            O0OOOOOO00OO0OO0O ={'key':O00000O00O0000O00 .key ,'type':'mtzyd'}#line:198
            OOOO0O00O00O00000 =requests .get (O0000O0O0O0OO0O0O ,params =O0OOOOOO00OO0OO0O ,timeout =3 )#line:199
            return OOOO0O00O00O00000 .text #line:200
        except Exception as O00OOO0O0O0000OO0 :#line:201
            print (O00000O00O0000O00 .name ,'查询状态异常',O00OOO0O0O0000OO0 )#line:202
            return False #line:203
    def user_info (O0OO0O000OO00OOOO ):#line:204
        OOO0OOOO0O0O0OO00 ='http://api2.wanjd.cn/h5_share/user/info'#line:205
        OOO0O0OO0O0OO0O00 =requests .post (OOO0OOOO0O0O0OO00 ,headers =O0OO0O000OO00OOOO .headers ,json ={"openid":0 })#line:206
        O0OO0O000OO00OOOO .printjson (OOO0O0OO0O0OO0O00 .text )#line:207
        OO00000OO0O0O000O =OOO0O0OO0O0OO0O00 .json ()#line:208
        if OO00000OO0O0O000O .get ('code')==200 :#line:209
            OO0OOO00OOO00000O =OO00000OO0O0O000O .get ('data').get ('nickname')#line:210
            OO00O000O0OOO0OOO =OO00000OO0O0O000O .get ('data').get ('points')#line:211
            O00OOOO0OO000000O =OO00000OO0O0O000O .get ('data').get ('used_points')#line:212
            O0OO0O000OO00OOOO .sy =OO00O000O0OOO0OOO -O00OOOO0OO000000O #line:213
            print (O0OO0O000OO00OOOO .name ,f'当前账号：{OO0OOO00OOO00000O},总积分积分：{OO00O000O0OOO0OOO}，已经提现：{O00OOOO0OO000000O},剩余：{O0OO0O000OO00OOOO.sy}')#line:214
        else :#line:215
            print (O0OO0O000OO00OOOO .name ,'获取账号信息异常,ck可能失效请重新获取')#line:216
            return False #line:217
    def sign (O0O0O00O00O000OOO ):#line:218
        OOO0O0O000OO00O00 ='http://api2.wanjd.cn/h5_share/user/sign'#line:219
        O0O0OO0O0OO0O0O00 =requests .post (OOO0O0O000OO00O00 ,headers =O0O0O00O00O000OOO .headers ,json ={"openid":0 })#line:220
        O0O0O00O00O000OOO .printjson (O0O0OO0O0OO0O0O00 .text )#line:221
        print (O0O0O00O00O000OOO .name ,'签到成功')#line:222
    def getMissions (OO0000OOOO00O0OOO ):#line:223
        O0OO0OOO00O0OO0OO ='http://api2.wanjd.cn/h5_share/daily/getMissions'#line:224
        OOOO00O0OO0OO00OO =requests .post (O0OO0OOO00O0OO0OO ,headers =OO0000OOOO00O0OOO .headers ,json ={"openid":0 })#line:225
        O00O000O0O0O00O0O =OOOO00O0OO0OO00OO .json ()#line:226
        if O00O000O0O0O00O0O .get ('code')!=200 :#line:227
            OO0000OOOO00O0OOO .printjson (OOOO00O0OO0OO00OO .text )#line:228
            return False #line:229
        O0000O0OOO0OOOO0O =''#line:230
        for O0OO0OOO0OO000000 in O00O000O0O0O00O0O .get ('data'):#line:231
            if O0OO0OOO0OO000000 .get ('title')=='文章阅读推荐':#line:232
                O0000O0OOO0OOOO0O =O0OO0OOO0OO000000 #line:233
                break #line:234
        if O0000O0OOO0OOOO0O =='':#line:235
            OO0000OOOO00O0OOO .printjson (OOOO00O0OO0OO00OO .text )#line:236
            print ('没有找到任务')#line:237
            return False #line:238
        OO0000OOOO00O0OOO .printjson (O0000O0OOO0OOOO0O )#line:239
        if O0000O0OOO0OOOO0O .get ('left_time')=='开始活动':#line:240
            return True #line:241
        else :#line:242
            print (OO0000OOOO00O0OOO .name ,'下次阅读,',end ='')#line:243
            print (OO0000OOOO00O0OOO .name ,O0000O0OOO0OOOO0O .get ('left_time'))#line:244
            return False #line:245
    def read_info (O0O00000O00000OOO ):#line:246
        O0OOOOOOO00O0O00O =f'http://api2.wanjd.cn/h5_share/daily/get_read'#line:247
        OO0OO00O0O00O0OOO =requests .post (O0OOOOOOO00O0O00O ,headers =O0O00000O00000OOO .headers ,json ={"openid":0 })#line:248
        O0OOOOO000O0O0000 =OO0OO00O0O00O0OOO .json ()#line:250
        if O0OOOOO000O0O0000 .get ('code')==200 :#line:251
            O00OOO000OO00O0OO =O0OOOOO000O0O0000 .get ('data').get ('link')#line:252
            OO0O0OOOOO00OO00O =urlparse (O00OOO000OO00O0OO ).netloc #line:253
            return O00OOO000OO00O0OO ,OO0O0OOOOO00OO00O #line:254
        else :#line:255
            print (O0O00000O00000OOO .name ,'获取阅读链接异常异常')#line:256
            print (O0O00000O00000OOO .name ,OO0OO00O0O00O0OOO .text )#line:257
            return False #line:258
    def gettaskinfo (OO0O0O0OO000O0O0O ,O0O0O0O0O0OOOO0OO ):#line:259
        for O00O00OO00OO00000 in O0O0O0O0O0OOOO0OO :#line:260
            if O00O00OO00OO00000 .get ('url'):#line:261
                return O00O00OO00OO00000 #line:262
        return False #line:263
    def read (O0O0O00OO000OOO0O ):#line:264
        print (O0O0O00OO000OOO0O .name ,'阅读开始')#line:265
        OOOO00OO00O00OO00 =O0O0O00OO000OOO0O .read_info ()#line:266
        if OOOO00OO00O00OO00 ==False :return False #line:267
        OOOOO000O0O000OOO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Content-Type':'application/x-www-form-urlencoded','Accept':'*/*','Origin':f'http://{OOOO00OO00O00OO00[1]}','Referer':f'http://{OOOO00OO00O00OO00[1]}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:276
        O0O0O00OO000OOO0O .num =0 #line:277
        O0OO000O0OOO0O0O0 =0 #line:278
        while True :#line:279
            print (O0O0O00OO000OOO0O .name ,'-'*50 )#line:280
            O0OOOOO00OOOOOOO0 ='https://api2.wanjd.cn/wxread/articles/tasks'#line:281
            OO00OOO0O00O00O00 ={'href':OOOO00OO00O00OO00 [0 ]}#line:282
            OOOOOO00O00O0O000 =requests .post (O0OOOOO00OOOOOOO0 ,headers =OOOOO000O0O000OOO ,data =OO00OOO0O00O00O00 )#line:283
            O0O0O00OO000OOO0O .printjson (OOOOOO00O00O0O000 .text )#line:284
            OOO000O0000OO0OOO =OOOOOO00O00O0O000 .json ()#line:285
            OO0O0OOOO000OOOO0 =OOO000O0000OO0OOO .get ('code')#line:286
            if OO0O0OOOO000OOOO0 ==500 :#line:287
                print (O0O0O00OO000OOO0O .name ,'阅读异常,获取任务失败')#line:288
                print (O0O0O00OO000OOO0O .name ,OOO000O0000OO0OOO .get ('data'))#line:289
                break #line:290
            if OO0O0OOOO000OOOO0 ==200 :#line:291
                OO0OO0O0OOO00000O =O0O0O00OO000OOO0O .gettaskinfo (OOO000O0000OO0OOO .get ('data'))#line:292
                if OO0OO0O0OOO00000O ==False :#line:293
                    print ('文章读完')#line:294
                    break #line:295
                O00OOO0000000OOO0 =OO0OO0O0OOO00000O .get ('url')#line:296
                OOO0OOOO00OO0O000 =OO0OO0O0OOO00000O .get ('id')#line:297
                O0O00O0OOO0O00O0O =getinfo (O00OOO0000000OOO0 )#line:298
                if O0O00O0OOO0O00O0O ==False :#line:299
                    push ('美添赚过检测',O00OOO0000000OOO0 ,'文章获取失败','mtzyd',O0O0O00OO000OOO0O .uids ,O0O0O00OO000OOO0O .key )#line:300
                    return False #line:301
                if O0O0O00OO000OOO0O .testCheck (O0O00O0OOO0O00O0O ,O00OOO0000000OOO0 )==False :#line:302
                    return False #line:303
                if O0OO000O0OOO0O0O0 ==0 :#line:304
                    OOO00O000000O0O0O =list (O0O00O0OOO0O00O0O )#line:305
                    OOO00O000000O0O0O [4 ]='oneischeck'#line:306
                    if O0O0O00OO000OOO0O .testCheck (OOO00O000000O0O0O ,O00OOO0000000OOO0 )==False :#line:307
                        return False #line:308
                    O0O0O00OO000OOO0O .num =len (OOO000O0000OO0OOO .get ('data'))#line:309
                    O0OO000O0OOO0O0O0 =1 #line:310
                OO0OO0O00O00000OO =random .randint (7 ,10 )#line:311
                print (O0O0O00OO000OOO0O .name ,f'本次模拟读{OO0OO0O00O00000OO}秒')#line:312
                time .sleep (OO0OO0O00O00000OO )#line:313
                O0OOOOO00OOOOOOO0 ='https://api2.wanjd.cn/wxread/articles/three_read'#line:314
                OO0O00OO00O0000OO ={'id':OOO0OOOO00OO0O000 ,'href':OOOO00OO00O00OO00 [0 ]}#line:315
                OOOOOO00O00O0O000 =requests .post (O0OOOOO00OOOOOOO0 ,headers =OOOOO000O0O000OOO ,data =OO0O00OO00O0000OO )#line:316
                O0O0O00OO000OOO0O .printjson (OOOOOO00O00O0O000 .text )#line:317
                O0O0O00OO000OOO0O .num -=1 #line:318
                print (O0O0O00OO000OOO0O .name ,'本轮剩余文章',O0O0O00OO000OOO0O .num )#line:319
            else :#line:320
                print (O0O0O00OO000OOO0O .name ,'阅读异常,获取任务失败')#line:321
                print (O0O0O00OO000OOO0O .name ,OOO000O0000OO0OOO )#line:322
                return False #line:323
        O0000O0O0O000OO00 ='https://api2.wanjd.cn/wxread/articles/check_success'#line:324
        O00000O000000OOOO ={'type':1 ,'href':OOOO00OO00O00OO00 [0 ]}#line:325
        OO000OOO00O0O0OO0 =requests .post (O0000O0O0O000OO00 ,headers =OOOOO000O0O000OOO ,data =O00000O000000OOOO )#line:326
        print ('任务结果',OO000OOO00O0O0OO0 .text )#line:327
        print (O0O0O00OO000OOO0O .name ,'本次阅读已完成')#line:328
    def testCheck (OO0O000000000O0OO ,OOO0OOO000OOO0O00 ,OOO000OOO00000000 ):#line:329
        if OOO0OOO000OOO0O00 [4 ]==[]:#line:330
            print (OO0O000000000O0OO .name ,'这个链接没有获取到微信号id',OOO000OOO00000000 )#line:331
            return True #line:332
        if checkDict .get (OOO0OOO000OOO0O00 [4 ])!=None :#line:333
            OO0O000000000O0OO .setstatus ()#line:334
            for O0O00OOO00OO0O000 in range (60 ):#line:335
                if O0O00OOO00OO0O000 %30 ==0 :#line:336
                    push ('美添赚过检测',OOO000OOO00000000 ,OOO0OOO000OOO0O00 [3 ],'mtzyd',OO0O000000000O0OO .uids ,OO0O000000000O0OO .key )#line:337
                O0OOO00OO0O00O000 =OO0O000000000O0OO .getstatus ()#line:338
                if O0OOO00OO0O00O000 =='0':#line:339
                    print (OO0O000000000O0OO .name ,'过检测文章已经阅读')#line:340
                    return True #line:341
                elif O0OOO00OO0O00O000 =='1':#line:342
                    print (OO0O000000000O0OO .name ,f'正在等待过检测文章阅读结果{O0O00OOO00OO0O000}秒。。。')#line:343
                    time .sleep (1 )#line:344
                else :#line:345
                    print (OO0O000000000O0OO .name ,O0OOO00OO0O00O000 )#line:346
                    print (OO0O000000000O0OO .name ,'服务器异常')#line:347
                    return False #line:348
            print (OO0O000000000O0OO .name ,'过检测超时中止脚本防止黑号')#line:349
            return False #line:350
        else :#line:351
            return True #line:352
    def withdraw (OO000O0OOO00O0O0O ):#line:353
        if OO000O0OOO00O0O0O .sy <1000 :#line:354
            print (OO000O0OOO00O0O0O .name ,'没有达到提现标准')#line:355
            return False #line:356
        OO0OO0OOOOOOOOOO0 ='http://api2.wanjd.cn/h5_share/user/withdraw'#line:357
        O00OO0O0OOO00OO0O =requests .post (OO0OO0OOOOOOOOOO0 ,headers =OO000O0OOO00O0O0O .headers )#line:358
        print (OO000O0OOO00O0O0O .name ,'提现结果',O00OO0O0OOO00OO0O .text )#line:359
    def run (O000OO0000O0O00OO ):#line:360
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='c2967ded72a713df3a213ef160edeb4b':O000OO0000O0O00OO .setstatus ()#line:361
        if O000OO0000O0O00OO .user_info ()==False :#line:362
            return False #line:363
        O000OO0000O0O00OO .sign ()#line:364
        if O000OO0000O0O00OO .getMissions ():#line:365
            O000OO0000O0O00OO .read ()#line:366
            O000OO0000O0O00OO .user_info ()#line:367
        time .sleep (2 )#line:368
        O000OO0000O0O00OO .withdraw ()#line:369
def getEnv (O00O0000OOOO0O00O ):#line:370
    O0OO00O000OO0OO00 =os .getenv (O00O0000OOOO0O00O )#line:371
    if O0OO00O000OO0OO00 ==None :#line:372
        print (f'{O00O0000OOOO0O00O}没有获取到，使用本地参数')#line:373
        return False #line:374
    try :#line:375
        O0OO00O000OO0OO00 =json .loads (O0OO00O000OO0OO00 .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:376
        return O0OO00O000OO0OO00 #line:377
    except Exception as OOO0OO0O00O00O0O0 :#line:378
        print ('错误:',OOO0OO0O00O00O0O0 )#line:379
        print ('你填写的变量是:',O0OO00O000OO0OO00 )#line:380
        print ('请检查变量参数是否填写正确')#line:381
        print (f'{O00O0000OOOO0O00O}使用本地参数')#line:382
if __name__ =='__main__':#line:383
    loc_push_config ={"printf":0 ,"threadingf":0 ,"appToken":"AT_9KCY75iQ8xxxxyu6JC"}#line:384
    loc_mtzconfig =[{'name':'备注名','Authorization':'share:login:55ea170xxxx9c4f7dac48','key':'4e9b9xxxx5f451f2a78a','uids':'UID_11ZxxxxUeq12lncQ'},]#line:389
    push_config =getEnv ('push_config')#line:391
    if push_config ==False :push_config =loc_push_config #line:392
    print (push_config )#line:393
    mtzconfig =getEnv ('mtzconfig')#line:394
    if mtzconfig ==False :mtzconfig =loc_mtzconfig #line:395
    print (mtzconfig )#line:396
    printf =push_config ['printf']#line:397
    appToken =push_config ['appToken']#line:398
    threadingf =push_config ['threadingf']#line:399
    getmsg ()#line:400
    tl =[]#line:401
    if threadingf ==1 :#line:402
        for cg in mtzconfig :#line:403
            print ('*'*50 )#line:404
            print (f'开始执行{cg["name"]}')#line:405
            api =MTZYD (cg )#line:406
            t =threading .Thread (target =api .run ,args =())#line:407
            tl .append (t )#line:408
            t .start ()#line:409
            time .sleep (0.5 )#line:410
        for t in tl :#line:411
            t .join ()#line:412
    elif threadingf ==0 :#line:413
        for cg in mtzconfig :#line:414
            print ('*'*50 )#line:415
            print (f'开始执行{cg["name"]}')#line:416
            api =MTZYD (cg )#line:417
            api .run ()#line:418
            print (f'{cg["name"]}执行完毕')#line:419
            time .sleep (3 )#line:420
    else :#line:421
        print ('请确定推送变量中threadingf参数是否正确')#line:422
    print ('全部账号执行完成')#line:423
    time .sleep (15 )#line:424
