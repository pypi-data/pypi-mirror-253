import json
import requests
import time
import random
from hashlib import md5
import tool


def index(coki,uid):
    
    url="https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/index"
    header={
	    "User-Agent":tool.agent('ipone'),
	    "Host":'api-takumi-record.mihoyo.com',
        "Cookie":coki,
        "DS":tool.final('4x','ds2',uid),
        "x-rpc-app_version":'2.52.1',
        "x-rpc-client_type":'5',
    }
    query_get={
        "role_id":uid,
        "server":'cn_gf01'
    }
    r=requests.get(url,headers=header,params=query_get)
    r=tool.retcode(r)
    ret=r['ret']
    if ret==0:
        r=r['data']
    elif ret==2:
        url='https://api-takumi-record.mihoyo.com/game_record/app/card/wapi/createVerification?is_high=true'
        cont=requests.get(url,headers=header,params=query_get)
        r=cont.text
    elif ret==1:
        r=r
    else:
        r='未预料到的错误'
    return r

def card(coki,uid):
    url='https://api-takumi-record.mihoyo.com/game_record/card/api/getGameRecordCard'
    header={
	    "User-Agent":tool.agent('ipone'),
	    "Host":'api-takumi-record.mihoyo.com',
        "Cookie":coki,
        "DS":tool.final('k2','ds1',uid),
        "x-rpc-app_version":'2.63.1',
        "x-rpc-client_type":'2',
    }
    query_get={
        'uid':uid,
    }
    r=requests.get(url,headers=header,params=query_get)
    r=tool.retcode(r)
    return r

def data(coki,uid):
    url='https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/roleBasicInfo'
    header={
	    "User-Agent":tool.agent('ipone'),
	    "Host":'api-takumi-record.mihoyo.com',
        "Cookie":coki,
        "DS":tool.final('4x','ds2',uid),
        "x-rpc-app_version":'2.63.1',
        "x-rpc-client_type":'5',
    }
    query_get={
        'server':'cn_gf01',
        'role_id':uid,
    }
    r=requests.get(url,headers=header,params=query_get)
    r=tool.retcode(r)
    return r