import json
import random
import time
from pprint import pprint

import pandas as pd
import requests
from pandas.io.json import json_normalize
from requests.exceptions import RequestException

page = 0


def main_info(page):
    base = "https://beta.sspai.com/api/v1/article/index/page/get?limit=10&offset={}".format(
        page)
    headers = {
        'User-AgentH':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    try:
        res = requests.get(base, headers=headers)
        if res.status_code in (200, 304):
            main_data = json.loads(res.text)['data']
            tidy_data = json_normalize(main_data)
            return tidy_data
        else:
            print('Something wrong has happended, status code is: %s' %
                  res.status_code)
    except requests.RequestException as e:
        print('Unable to get page content: %s' % e)


def concat_data(page):
    random.seed(random._pi)
    all_data = {}
    while True:
        if page <= 12210:
            all_data['page%s' % page] = main_info(page)
            print('Get page %s data...' % page)
            page += 1
            time.sleep(random.random() * random._pi)
        else:
            print('Stop running!')
            break

    return all_data


if __name__ == "__main__":
    all_data = concat_data(page)
    final_data = pd.concat([data for data in all_data.values()],
                           ignore_index=True)
    final_data.to_excel(r'./page_data.xlsx', index=False)
