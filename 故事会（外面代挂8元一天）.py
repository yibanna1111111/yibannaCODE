#此脚本入口易进群
#变量为huodong_id=""uid=""Authorization=""
#交流群：949598994
import json
import requests
import urllib.parse


huodong_id=""
uid=""
Authorization=""
url = 'http://hb2.hbdtxt.com/api/index/index'
headers = {
    'Authorization': Authorization,
    'User-Agent': '/5.0 (Linux; Android 9; NX629J_V1S Build/PQ3A.190705.09211555; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 MMWEBID/2157 MicroMessenger/8.0.41.2460(0x28002A54) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://hb2.hbdtxt.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 's342b0066=tu7bbcn9brab7rhosb27jomff3'
}

data = {
    'huodong_id': huodong_id,
    'ids': '',
    'api_type': 'h5',
    'uid': uid
}


response = requests.post(url, headers=headers, data=data)

response_content = response.content.decode('utf-8')
print(response.text)

response_data = json.loads(response_content)


code = response_data['code']
msg = response_data['msg']
canyu_status = response_data['canyu_status']
is_can = response_data['is_can']
huodong = response_data['huodong']
wentilist = response_data['wentilist']


modified_wentilist = []

for question in wentilist:
    daan = json.loads(question["daan"])[0] 
    for option in question["xuanxiang"]:
        if option["xuhao"] == daan:
            option["xuanzhong"] = 1
        else:
            option["xuanzhong"] = 0
    modified_wentilist.append(question)


print(f"wentilist={json.dumps(modified_wentilist, ensure_ascii=False)}")

data = json.dumps(modified_wentilist, ensure_ascii=False)


encoded_data = urllib.parse.quote(data)


a=f"wentilist={encoded_data}&huodonq_id={huodong_id}&ids=&api_type=h5&uid={uid}"
url1='httd://hb2.hbdtxt.com/api/index/dati'
response = requests.post(url1, headers=headers, data=a)
print(response.text)