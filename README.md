# 文件概述 

## 整个项目的目录结构

```
.
.
├── README.md
├── analysis
│   ├── base_analysis.ipynb
│   └── title_NLP.ipynb
├── data
│   ├── page_data.xlsx
│   ├── stopwords.txt
│   ├── user_data.xlsx
│   └── user_dict.txt
└── spider
    ├── sspai.py
    └── sspai_user_info.pyy
```

## 文件详情

- `data`：
  - `page_data.xlsx`：存放爬取到的首页数据
  - `user_data.xlsx`：存放用户页面的相关数据
  - `stopwords.txt`：分词的停止词
  - `user_dict.txt`：自定义字典，使分词时准确切分
- `spider`：
    - `sspai_user_info.py`：用于获取用户页成就的相关数据
    - `sspai.py`：主要的爬虫程序，通过少数派自己的api访问并获取首页文章的相关数据
- `analysis`：
  - `base_analysis.ipynb`：数据分析的 Notebook
  - `title_NLP.ipynb`：标题的自然语言处理部分