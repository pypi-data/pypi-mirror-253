import time
import random
import json
import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from hashlib import md5
import base64


def agent(type):
    if type=='iphone':
        cont='Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.11.1)'
    else:
        cont='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'
    return cont

def rsa(key,cont):
    key = key.encode('utf-8')
    # 反序列化PEM格式的公钥
    public_key = serialization.load_pem_public_key(key, backend=default_backend())

    # 将内容转换为字节
    message = cont.encode('utf-8')

    # 使用公钥加密消息
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 返回加密后的结果
    return ciphertext.hex()


def final(type,typ,uid):
    if type=='4x' and typ=='ds2':
        salt = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
        query = "&".join(sorted(f"server=cn_gf01&role_id={uid}".split("&")))
        t = int(time.time())
        r = random.randint(100001, 200000)
        main = f"salt={salt}&t={t}&r={r}&b=&q={query}"
        ds = md5(main.encode(encoding='UTF-8')).hexdigest()
        final = f"{t},{r},{ds}"
    elif type=="k2" and typ=='ds1':
        lettersAndNumbers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        salt = "BIPaooxbWZW02fGHZL1If26mYCljPgst"   
        t = int(time.time())
        r = "".join(random.choices(lettersAndNumbers, k=6))
        main = f"salt={salt}&t={t}&r={r}"
        ds = md5(main.encode(encoding='UTF-8')).hexdigest()
        final = f"{t},{r},{ds}" 
    else:
        final='没有这样的组合'
    return final

def retcode(retcode):
    r=retcode.text
    r_o=json.loads(r)
    retcode=r_o['retcode']
    if retcode==0:
        cont=r.text
        ret=1
        r={'ret':ret,'data':cont}
    elif retcode==1034:
        data='遇到验证码'
        ret=2
        r={'ret':ret,'data':data,'cont':r}
    elif retcode==10102:
        ret=0
        cont='未开启展示'
        r={'ret':ret,'data':cont}
    return r