# DAY 19

import statistics
import requests
import pandas
import json
import sys
import re

# LEVEL 2

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()


min_weight = sys.maxsize
max_weight = 0
mean_weight = 0
median_weight = 0
std_weight = 0
weight_lst = list()
countries = list()

for cat in cats:
    str_weight = cat.get('weight').get('metric')
    weights = re.findall(r'\d{1,2}', str_weight)
    x = int(weights[0])
    y = int(weights[1])
    sum_weight = (x + y) / 2
    if(sum_weight > max_weight):
        max_weight = sum_weight
    if(sum_weight < min_weight):
        min_weight = sum_weight
    weight_lst.append(sum_weight)
    countries.append(cat.get('origin'))

lst_length = len(weight_lst)
data = pandas.Series(countries)

for i in range(lst_length):
    for j in range(0, lst_length - i - 1):
        if(weight_lst[j] > weight_lst[j + 1]):
            tmp = weight_lst[j]
            weight_lst[j] = weight_lst[j + 1]
            weight_lst[j + 1] = tmp

mean_weight = (sum(weight_lst)) / lst_length

if(lst_length % 2 == 0):
   median_weight = (weight_lst[lst_length / 2] + weight_lst[(lst_length / 2) + 1]) / 2
else:
    median_weight = weight_lst[lst_length // 2]
    
std_weight = statistics.stdev(weight_lst)

print(f'Max: {max_weight}\nMin: {min_weight}')
print('Mean: ', mean_weight)
print('Median: ', median_weight)
print('Std: ', std_weight)

print('Frequency Table for the data : ')
print(data.value_counts())


# LEVEL 3

with open('../data/countries_data_long.json') as f:
    txt = f.read()
    countries = json.loads(txt)

languages_set = set()
for country in countries:
    for language in country.get('languages'):
        languages_set.add(language.get('name'))

print('Total languages: ', len(languages_set))
print(languages_set)
