#!usr/bin/env python
#coding:utf-8

import requests
import json
import pandas as pd
from pprint import pprint
from requests.exceptions import RequestException

def user_info(slug):
    base = 'https://beta.sspai.com/api/v1/user/slug/info/get?slug={}'.format(str(slug))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 
        'Referer': 'https://beta.sspai.com/u/{}/updates'.format(str(slug))
    }
    
    user_infos = {}
    try: 
        res = requests.get(base, headers = headers)
        json_data = json.loads(res.text)
        #TODO: pandas.io.json.json_normalize()
        user_infos['view_count'] = json_data['data']['article_view_count']
        user_infos['word_count'] = json_data['data']['articles_word_count'] 
        user_infos['like_count'] = json_data['data']['liked_count']
        user_infos['create_at'] = json_data['data']['created_at']
        user_infos['followers_num'] = json_data['data']['followed_count']        
        if len(json_data['data']['user_flags']) > 0:
            user_infos['occupation1'] = json_data['data']['user_flags'][0]['name']
            user_infos['occupation2'] = json_data['data']['user_flags'][1]['name']
        else:
            user_infos['occupation1'] = ''
            user_infos['occupation2'] = ''

        pprint(user_infos)

    except RequestException as e:
        print('unable to get page content: %s' %e)

    return user_infos

if __name__ == "__main__":

    data = pd.read_excel(r'./data/page_data.xlsx')
    data['author.slug'] = data['author.slug'].str.replace('0lf47ddk', 'sunsetye') #异常值处理

    # 用户数据获取
    slugs = data['author.slug'].unique().tolist()
    user_data = {}
    for slug in slugs:
        user_data[slug] = user_info(slug)

    user_data = (pd.DataFrame(user_data)
                .T
                .reset_index()
                .rename(columns={'index':'author_slug'}))

    user_data.to_excel(r'./data/user2_data.xlsx', index=False)
