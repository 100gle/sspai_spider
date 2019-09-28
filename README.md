# 文件概述 

## 整个项目的目录结构

```
.
├── README.md
├── __pycache__
│   └── sspai_user_info.cpython-37.pyc
├── analysis.py
├── data
│   ├── page_data.xlsx
│   ├── stopwords.txt
│   └── user_dict.txt
├── sspai.py
└── sspai_user_info.py
```

## 文件详情

- `data`：文件夹中主要存放的是首页的爬取数据、以及分词使用的停止词和字典
- `sspai_user_info.py`：用于获取用户页成就的相关数据
- `sspai.py`：主要的爬虫程序，通过少数派自己的api访问并获取首页文章的相关数据
- `analysis.py`：数据分析与可视化部分