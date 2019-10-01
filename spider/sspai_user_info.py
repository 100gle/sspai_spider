#!usr/bin/env python
#coding:utf-8

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint
from requests.exceptions import RequestException

def user_info(slug):
    base = 'https://beta.sspai.com/api/v1/user/slug/info/get?slug={}'.format(str(slug))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 
        'Referer': 'https://beta.sspai.com/u/{}/updates'.format(str(slug))
    }
    
    user_infos = {}
    all_data = pd.DataFrame()
    try: 
        res = requests.get(base, headers = headers)
        json_data = json.loads(res.text)

        user_infos['data.slug'] = json_data['data']['slug']
        if len(json_data['data']['user_flags']) == 2:
            user_infos['data.occupation1'] = json_data['data']['user_flags'][0]['name']
            user_infos['data.occupation2'] = json_data['data']['user_flags'][1]['name']
        elif len(json_data['data']['user_flags']) == 1:
            user_infos['data.occupation1'] = json_data['data']['user_flags'][0]['name']
            user_infos['data.occupation2'] = ''
        else:
            user_infos['data.occupation1'] = ''
            user_infos['data.occupation2'] = ''
        all_data = pd.merge(json_normalize(json_data),
                            json_normalize(user_infos), 
                            on='data.slug')
        pprint(all_data)
        return all_data

    except RequestException as e:
        print('unable to get page content: %s' %e)

if __name__ == "__main__":
    data = pd.read_excel(r'./data/page_data.xlsx') #Windows用户需要修改路径
    data['author.slug'] = data['author.slug'].str.replace('0lf47ddk', 'sunsetye') #异常值处理

    # 用户数据获取
    slugs = data['author.slug'].unique().tolist()
    user_data = {}
    for slug in slugs:
        user_data[slug] = user_info(slug)
    user_data = pd.concat([data for data in user_data.values()])
    user_data.to_excel(r'./data/user_data.xlsx', index=False)