"""
@Qim��Ʒ ����ѧϰ�������������غ��24Сʱ����ȫɾ�� �����κ�����������ҵ��Ƿ�Ŀ�ģ��������Ը���
���G�Ķ��Ķ�_V1.63   ��ڣ�http://2565577.h1nvfu.gbl.9el89729wwqg.cloud/?p=2565577
�Ķ�����ץ��cookie���Ҳ�������gfsessionid�ؼ��ʣ�
export ydtoken=cookie
���˺���'===='���� �� �˺�1====�˺�2
cron��23 7-23/3 * * *
"""

max_concurrency = 5  # �����߳���
money_Withdrawal = 0  # ���ֿ��� 1���� 0�ر�
key = ""        #keyΪ��ҵ΢��webhook�����˺���� key








import re
import hashlib
import json
import os
import random

import threading
import time
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import requests

lock = threading.Lock()


def process_account(account, i):
    values = account.split('@')
    cookie = values[0]

    print(f"\n=======��ʼִ���˺�{i}=======")
    current_time = str(int(time.time()))

    sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Cookie": cookie
    }

    data = {
        "time": current_time,
        "sign": sign
    }

    with lock:
        response = requests.get(url, headers=headers, json=data).json()
        share_link = response['data']['share_link'][0]
        p_value = share_link.split('=')[1].split('&')[0]

        url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/read/info"

        response = requests.get(url, headers=headers, json=data).json()

        if response['code'] == 0:
            remain = response['data']['remain']
            read = response['data']['read']
            print(f"ID:{p_value}-----���G���:{remain}\n�����Ķ���::{read}\n�ƹ�����:{share_link}")
        else:
            print(response['message'])

    print("============��ʼִ���Ķ�����============")

    for j in range(30):
        biz_list = ['MzkyMzI5NjgxMA==', 'MzkzMzI5NjQ3MA==', 'Mzg5NTU4MzEyNQ==', 'Mzg3NzY5Nzg0NQ==',
                    'MzU5OTgxNjg1Mg==', 'Mzg4OTY5Njg4Mw==', 'MzI1ODcwNTgzNA==','Mzg2NDY5NzU0Mw==']
        # ���� sign
        sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
        sha256_hash = hashlib.sha256(sign_str.encode())
        sign = sha256_hash.hexdigest()
        url = "http://2477726.9o.10r8cvn6b1.cloud/read/task"

        try:
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        except requests.Timeout:
            print("����ʱ���������·�������...")
            response = requests.get(url, headers=headers, json=data, timeout=7).json()
        if response['code'] == 1:
            print(response['message'])
            break
        else:
            try:
                mid = response['data']['link'].split('&mid=')[1].split('&')[0]
                biz = response['data']['link'].split('__biz=')[1].split('&')[0]

                print(f"[{p_value}]��ȡ���³ɹ�---{mid} ��Դ[{biz}]")

                if biz in biz_list:
                    print(f"����Ŀ��[{biz}] ���Ƽ�����£�����")
                    link = response['data']['link']
                    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

                    messages = [
                        f"���ּ�����£�����\n{link}\n����60s�ڵ����������Ķ�",
                    ]

                    for message in messages:
                        data = {
                            "msgtype": "text",
                            "text": {
                                "content": message
                            }
                        }
                        headers = {'Content-Type': 'application/json'}
                        response = requests.post(url, headers=headers, data=json.dumps(data))
                        print("�Խ�������������΢������60s�ڵ����������Ķ�--60s���������")
                        time.sleep(60)
                        url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                            "Cookie": cookie
                        }
                        data = {
                            "time": current_time,
                            "sign": sign
                        }
                        try:
                            response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        except requests.Timeout:
                            print("����ʱ���������·�������...")
                            response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        if response['code'] == 0:
                            gain = response['data']['gain']
                            print(f"��{j + 1}���Ķ�������³ɹ�---��ø��G[{gain}]")
                            print(f"--------------------------------")
                        else:
                            print(f"�����ʧ�ܣ��볢����������")
                            break
                else:
                    sleep = random.randint(8, 11)
                    print(f"����ģ���Ķ�{sleep}��")
                    time.sleep(sleep)
                    url = "http://2477726.9o.10r8cvn6b1.cloud/read/finish"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Linux; Android 9; V1923A Build/PQ3B.190801.06161913; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 MMWEBID/5635 MicroMessenger/8.0.40.2420(0x28002837) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
                        "Cookie": cookie
                    }
                    data = {
                        "time": current_time,
                        "sign": sign
                    }
                    try:
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    except requests.Timeout:
                        print("����ʱ���������·�������...")
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    if response['code'] == 0:
                        gain = response['data']['gain']
                        print(f"��{j + 1}���Ķ����³ɹ�---��ø��G[{gain}]")
                        print(f"--------------------------------")
                    else:
                        print(f"�Ķ�����ʧ��{response}")
                        break
            except KeyError:
                print(f"��ȡ����ʧ��,����δ֪{response}")
                break
    if money_Withdrawal == 1:
        print(f"============��ʼ΢������============")
        url = "http://2477726.84.8agakd6cqn.cloud/withdraw/wechat"

        response = requests.get(url, headers=headers, json=data).json()
        if response['code'] == 0:
            print(response['message'])
        elif response['code'] == 1:
            print(response['message'])
        else:
            print(f"����δ֪{response}")
    elif money_Withdrawal == 0:
        print(f"{'-' * 30}\n��ִ������")


if __name__ == "__main__":
    accounts = os.getenv('ydtoken')
    if accounts is None:
        print('��û������ydtoken��զ���У�')
    else:
        response = requests.get('https://netcut.cn/p/e9a1ac26ab3e543b')
        note_content_list = re.findall(r'"note_content":"(.*?)"', response.text)
        formatted_note_content_list = [note.replace('\\n', '\n').replace('\\/', '/') for note in note_content_list]
        for note in formatted_note_content_list:
            print(note)
        accounts_list = os.environ.get('ydtoken').split('====')
        num_of_accounts = len(accounts_list)
        print(f"��ȡ�� {num_of_accounts} ���˺�")
        with Pool(processes=num_of_accounts) as pool:
            thread_pool = ThreadPool(max_concurrency)
            thread_pool.starmap(process_account, [(account, i) for i, account in enumerate(accounts_list, start=1)])
