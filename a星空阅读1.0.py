import requests
import config

def push(name, link, text, acttype, uids,key):
    summary = name + ':' + config.dictType.get(acttype)
    appToken = config.appToken
    str1 = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>过检测</title>
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
    '''
    content = str1.replace('LINK', link).replace('TEXT', text).replace('TYPE', acttype).replace('KEY', key)
    datapust = {
        "appToken": appToken,
        "content": content,
        "summary": summary,
        "contentType": 2,
        "uids": uids.split('|'),
        "url": "https://t.me/bwersgt",
    }
    urlpust = 'http://wxpusher.zjiecode.com/api/send/message'
    try:
        p = requests.post(url=urlpust, json=datapust).text
        print(p)
        print('推送成功')
        return True
    except Exception as e:
        print(e)
        print('推送失败！')
        return False
