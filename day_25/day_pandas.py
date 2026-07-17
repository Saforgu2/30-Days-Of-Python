# DAY 25

import pandas as pd
import numpy as np

# LEVEL 1

news_df = pd.read_csv('../data/hacker_news.csv')

print(news_df.head())

print('='*100)

print(news_df.tail())

print('='*100)

titles = news_df['title']
print(titles)

print('='*100)

shape = news_df.shape
print('Rows: ', shape[0])
print('Columns: ', shape[1])

print('='*100)

titles_with_python = list()
for title in titles:
    if('python' in title.lower()):
        titles_with_python.append(title)
print(titles_with_python)

print('='*100)

titles_with_javascript = list()
for title in titles:
    if('javascript' in title.lower()):
        titles_with_javascript.append(title)
print(titles_with_javascript)

print('='*100)
