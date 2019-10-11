import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_info(article_id):
    url = 'https://beta.sspai.com/post/{}'.format(str(article_id))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'html.parser')
    contentTag = soup.find('div', class_ = 'content wangEditor-txt')
    contents = contentTag.get_text()
    print('正在获取id%s的文章' %article_id)
    return contents

if __name__ == "__main__":
    data = pd.read_excel(r'D:\Project\myGit\sspai_spider\data\page_data.xlsx', usecols=['id'])
    article_id = data['id'].values.tolist()
    articles = {}
    for id_ in article_id:
        articles[str(id_)] = get_info(id_)
    articles_data = (pd.Series(articles)
                       .reset_index()
                       .rename(columns = {'index':'id', 
                                            0:'content'})
                    )
    articles_data.to_excel('article_content.xlsx', index=False)
