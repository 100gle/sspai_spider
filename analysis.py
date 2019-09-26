import pandas as pd
import jieba
from sspai_user_info import *
from collections import Counter

# 读入数据，并查看数据
data = pd.read_excel(r'./data/page_data.xlsx')
data.info()
data.head()

# 字段处理
cols = [
    'id', 'title', 'comment_count', 'like_count', 'view_count',
    'released_time', 'author.slug', 'author.nickname'
]
data = data[cols]
data.released_time = pd.to_datetime(data['released_time'], unit='s')
data.columns = data.columns.str.replace('.', '_')

# 用户画像
## 用户成就数据获取
slug = data.author_slug.unique().tolist()
user_data = {}
for auth in slug:
    user_data[auth] = user_info(auth)
user_data = (pd.DataFrame(user_data)
             .T
             .reset_index()
             .rename(columns={'index':'author_slug'}))


# 分词
# jieba.load_userdict() 添加自定义词库

stopwords = ''
def word_cut(text):
    words = jieba.lcut(text)
    title = []
    for word in words:
       if word not in stopwords:
          title.append(word) 
    return ' '.join(title)

data['title_cut'] = data['title'].apply(lambda title: word_cut(title))

all_ = ' '.join(data.title_cut.tolist())
title_words = Counter(jieba.lcut(all_))

from pyecharts.charts import WordCloud
from pyecharts.options import options as opts