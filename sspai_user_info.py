import requests
import pprint
import json
from bs4 import BeautifulSoup

#TODO: api need to be changes
base = 'https://beta.sspai.com/api/v1/user/slug/info/get?slug=100gle'


#TODO: Referer need to be changes
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 
    'Referer': 'https://beta.sspai.com/u/100gle/updates'}

res = requests.get(base, headers= headers)

json_data = json.loads(res.text)
pprint.pprint(json_data)

#TODO: user infos
view_count = json_data['data']['article_view_count']
word_count = json_data['data']['articles_word_count']
like_count = json_data['data']['liked_count']
create_at = json_data['data']['created_at']
followers_num = json_data['data']['followed_count']

