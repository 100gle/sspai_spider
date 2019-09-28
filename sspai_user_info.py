#!usr/bin/env python
#coding:utf-8

import requests
import json
from pprint import pprint
from requests.exceptions import RequestException

def user_info(slug):
    base = 'https://beta.sspai.com/api/v1/user/slug/info/get?slug={}'.format(str(slug))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 
        'Referer': 'https://beta.sspai.com/u/{}/updates'.format(str(slug))
    }
    try: 
        res = requests.get(base, headers= headers)
        json_data = json.loads(res.text)

        user_info = {}
        user_info['view_count'] = json_data['data']['article_view_count']
        user_info['word_count'] = json_data['data']['articles_word_count'] 
        user_info['like_count'] = json_data['data']['liked_count']
        user_info['create_at'] = json_data['data']['created_at']
        user_info['followers_num'] = json_data['data']['followed_count']        
        pprint(user_info)

        return user_info

    except RequestException as e:
        print('unable to get page content: %s' %e)

if __name__ == "__main__":
    slug='100gle'
    user_info(slug)