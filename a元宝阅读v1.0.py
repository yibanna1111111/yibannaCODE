'''
这个文件是总配置文件，请仔细读配置说明
多对多推送需要每个账号都关注推送的应用，注意主题和应用的区别
多对多推送仅需要每个账号填自己对应的一个uids，一个uids请不要用” | “,因为隔不开空气
一对多推送请用” | “隔开每个用户的uids,使用场景，把当前账号的过检测文章推给多个账号读，增加过检测概率
打开链接：https://wxpusher.zjiecode.com/admin/main/app/appFollow
能够找到应用关注码
'''
'''
czgmconfig是充值购买的参数配置列表
活动入口,微信打开：http://2478987.epghgkvalp.wjbk.25obcxyume.cloud/?p=2478987
打开活动入口，抓包的任意接口cookies中的gfsessionid参数,填入ck。
单账户填写样式。(这里只是样式，不要填这里)
czgmconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
czgmconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口cookies中的gfsessionid参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
'''
czgmconfig = [
    {'name': 'xxx', 'ck': 'o-0fIv9eJPxxxxxxUCNumg', "uids": 'UID_Yxxxxx2Kk|xxxx','key':'4edaca6803xxxxx05e1'},
    {'name': 'xxx', 'ck': 'o-0fIv8xxxxx34dk', "uids": 'UID_gdQlhxxxxxxfJxnPdwQ','key':'80257xxxxxb2c05257'},
    {'name': 'xxx', 'ck': 'o-0fxxxxxxtDlWc', "uids": 'UID_eYwmxxxxxxOPWoOc','key':'b6c948xxxxx502b624a6'},
]
#########################################################################
'''
mtzconfig是美添赚的参数配置列表
活动入口,微信打开：http://tg.1693182678.api.mengmorwpt2.cn/h5_share/ads/tg?user_id=115772
打开活动入口，抓包的任意接口headers中的Authorization参数，填入ck。
单账户填写样式(这里只是样式，不要填这里)
mtzconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
mtzconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用户uids可以单个推送消息给用户
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
'''
mtzconfig = [
    {'name': 'my', 'ck': 'share:login:xxxx', "uids": 'uid|uidxxx','key':'xxxx'},
    #{'name': 'xxxxx', 'ck': 'share:login:xxxxx', "uids": 'xxxxx','key':'xxxx'},
    #{'name': 'xxxxx', 'ck': 'share:login:xxxx', "uids": 'xxxxx','key':'xxxx'},
]
#########################################################################
'''
xyyconfig是小阅阅的参数配置列表
活动入口,微信打开：https://wib.quannengjiaoyu.top:10265/yunonline/v1/auth/693f35a37d8da489478562a1feab678f?codeurl=wib.quannengjiaoyu.top:10265&codeuserid=2&time=1693118713
打开活动入口，抓包的任意接口cookies中的ysm_uid参数,填入ck。
单账户填写样式(这里只是样式，不要填这里)
xyyconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
xyyconfig = [
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
    {'name': 'xxxx', 'ck': 'xxxx', "uids": 'UID_xxx|UID_xxx|UID_xxx','key':'xxxx'},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用过uids可以单个推送消息给用户
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
'''
xyyconfig = [
    {'name': 'dy', 'ck': 'oZdBpNI', "uids": 'UID_k','key':'4edacae1'},
    {'name': 'smh', 'ck': 'oZdBp2_gA', "uids": 'UID_dwQ','key':'802557'},
    {'name': 'ly', 'ck': 'oZdB1kc', "uids": 'UID_eYwoOc','key':'b6c948a6'},
]
#########################################################################
'''
xkybconfig是星空和元宝的共用参数配置列表，因为是一个平台，所以参数一样
活动入口,微信打开
星空阅读阅读：http://mr1692169663544.uznmvev.cn/ox/index.html?mid=XG7QUVEEH
元宝阅读：http://mr1693542990524.obmxvbv.cn/coin/index.html?mid=RG5RC7LDU
打开活动入口，抓包的http://u.cocozx.cn/api/ox/info接口的请求体中的un和token参数
单账户填写样式(这里只是样式，不要填这里)
xyyconfig = [
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx','key':'xxxx'},
]
多账户填写样式，几个账号填几个，不要多填。(这里只是样式，不要填这里)
xkybconfig = [
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'UIDxxx|UIDxxx|UIDxxx','key':'xxxx'}},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx','key':'xxxx'}},
    {'name': 'xxx', 'un': 'xxx', 'token': 'xxx',"uids": 'xxx','key':'xxxx'}},
]
参数解释
name:账号名，你可以随便填，用来推送时分辨哪一个账号
ck:账号的ck,抓包的任意接口headers中的Authorization参数
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送主题后，会在主题的关注列表中显示
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 用户管理->用户列表 能看到uids，用过uids可以单个推送消息给用户
key:每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
'''
xkybconfig = [
    #{'name': 'xxxx', 'un': 'oC34q66oUyxxxxw', 'token': 'xxxx',"uids": 'UIDxxxx','key':'xxxx'},
    #{'name': 'xxxx', 'un': 'oC34q696xxxx', 'token': 'xxxx',"uids": 'UID_gdQxxxx','key':'xxxx'},
    {'name': 'ly', 'un': 'oC34q6w4exixegYFUYez-qtMlxwU', 'token': 'ba15b22df3c485e3c62298cc3f753272',"uids": 'UID_eYwm1mIs0X7nZpVlu6lgqQOPWoOc','key':'b6c948772f1f953b14d441c502b624a6'},
]
#########################################################################
'''
公共推送参数
参数解释
appToken:wxpusher的参数，在你创建应用的过程中，你应该已经看到appToken，如果没有保存，可以通过下面的方式重制它。
打开链接：https://wxpusher.zjiecode.com/admin/main/topics/list点击 应用管理->appToken->重置appToken
'''
appToken = 'xxxxx'
#########################################################################
'''
其他参数
参数解释
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
printf:日志打印参数，0是不打印调试日志，1是打印调试日志
dictType:标志参数请勿修改
'''
threadingf=1
printf = 1
dictType = {
    'czgm': '充值购买过检测',
    'mtzyd': '美添赚过检测',
    'xyyyd': '小阅阅过检测',
    'ybxkhh': '星空元宝过检测',
    'yuanbao': '元宝过检测',
    'xingkong': '星空过检测'
}
#ybtxbz:元宝阅读提现标准，默认3000币时提现
ybtxbz=3000
#xktxbz:星空阅读提现标准，默认3000币时提现
xktxbz=3000
#czgmtxbz:充值购买阅读提现标准，默认3000币时提现
czgmtxbz=3000
#xyytxbz:小阅阅阅读提现标准，默认3000币时提现
xyytxbz=3000
