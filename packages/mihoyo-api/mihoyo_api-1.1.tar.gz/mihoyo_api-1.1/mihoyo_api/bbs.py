import json
import requests
import time
import tool
from geetest import get_validate

#cookie所属的游戏账号
def game_data(coki):
    url="https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie"
    header={
	    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62",
	    "Cookie":coki,
    }
    r=requests.get(url,headers=header)
    r=r.text
    r=json.loads(r)
    game_0=r['data']
    game_0=game_0['list']
    #数组个数/游戏数
    num=len(game_0)
    #将数据赋值
    for index,dictionary in enumerate(game_0,start=1):
        game_name=dictionary['game_biz']
        if game_name == 'bh3_cn':
            gamename='崩坏3国服'
        elif game_name == 'hk4e_cn':
            gamename='原神国服'
        elif game_name == 'hkrpg_cn':
            gamename='崩坏星穹铁道-国服'
        else:
            game_name=game_name
        locals()[f'game_{index}_gamename']=gamename
        locals()[f'game_{index}_uid']=dictionary['game_uid']
        locals()[f'game_{index}_name']=dictionary['nickname']
        locals()[f'game_{index}_server']=dictionary['region_name']
        locals()[f'game_{index}_level']=dictionary['level']
        locals()[f'game_{index}_region']=dictionary['region']
    #作为字典输出
    all_games_info = {}

    for index in range(1, num + 1):
        current_game_info = {
            'gamename': locals()[f'game_{index}_gamename'],
            'region': locals()[f'game_{index}_region'],
            'uid': locals()[f'game_{index}_uid'],
            'name': locals()[f'game_{index}_name'],
            'server': locals()[f'game_{index}_server'],
            'level': locals()[f'game_{index}_level'],
        }

        all_games_info[f'game_{index}'] = current_game_info
    output_str=''
    for key, value in all_games_info.items():
        output_str += f"游戏{key.split('_')[1]}:\n"
        for item_key, item_value in value.items():
            output_str += f"  {item_key}: {item_value}\n"
    return output_str
#账号数量
def game_num(coki):
    url="https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie"
    header={
	    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62",
	    "Cookie":coki,
    }
    r=requests.get(url,headers=header)
    r=r.text
    r=json.loads(r)
    game_0=r['data']
    game_0=game_0['list']
    #数组个数/游戏数
    num=len(game_0)
    return num

def login(acc,pas):
    url='https://webapi.account.mihoyo.com/Api/create_mmt'
    header={
	    "User-Agent":tool.agent('ipone'),
    }
    t = int(time.time())
    query_get={
        "scene_type":'1',
        "now":t,
        "reason":'user.mihoyo.com%2523%252Flogin%252Fpassword',
        "action_type":"login_by_password",
        "t":t
    }
    r=requests.get(url,headers=header,params=query_get)
    r_o=json.loads(r.text)
    r_type=r_o['data']['mmt_type']
    if r_type==0:
        r_key=r_o['data']['mmt_data']['mmt_key']
        url='https://api-takumi.mihoyo.com/account/auth/api/webLoginByPassword'
        header={
	        "User-Agent":tool.agent('ipone'),
        }
        #pas=tool.rsa('-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDvekdPMHN3AYhm/vktJT+YJr7cI5DcsNKqdsx5DZX0gDuWFuIjzdwButrIYPNmRJ1G8ybDIF7oDW2eEpm5sMbL9zs9ExXCdvqrn51qELbqj0XxtMTIpaCHFSI50PfPpTFV9Xt/hmyVwokoOXFlAEgCn+QCgGs52bFoYMtyi+xEQIDAQAB-----END PUBLIC KEY-----',pas)
        query_get={
            'account':acc,
            'password':pas,
            'mmt_key':r_key,
            'token_type':'6'
        }
        r=requests.get(url,headers=header,params=query_get)
        r=r.text
    else:
        gt=r['data']['mmt_data']['gt']
        challenge=r['data']['mmt_data']['challenge']
        validate=''
        challenge,validate=get_validate(gt,challenge)
        vali=len(validate)
        if vali != 0:
            r=requests.get(url,headers=header,params=query_get)
            r=r['retcode']
            if r==0:
                r='遇到验证码，破解成功！'
            else:
                r='遇到验证码，未破解成功'
        else:
            r='遇到验证码，未破解成功'
    return r