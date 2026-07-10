# DAY 19

import json
import csv
import re

# LEVEL 1

def read_files_txt(filename):
    print('File name: ', filename)
    f = open(filename)
    lines = f.readlines()
    characters = sum(len(i.split()) for i in lines)
    print('Lines: ', len(lines))
    print('Wrods: ', characters)
    f.close()

read_files_txt('../data/obama_speech.txt')
read_files_txt('../data/michelle_obama_speech.txt')
read_files_txt('../data/donald_speech.txt')
read_files_txt('../data/melina_trump_speech.txt')

def most_spoken_languages(filename, count):
    with open(filename) as f:
        text = f.read()
        countries_dct = json.loads(text)
        languages = list()
        for country in countries_dct:
            for language in country.get('languages'):
                if(len(languages) == 0):
                    languages.append([1, language])
                else:
                    i = 0
                    found = False
                    while(not found and i < len(languages)):
                        if(languages[i][1] == language):
                            languages[i][0] += 1
                            found = True
                        else:
                            i +=1
                    if(not found):
                        languages.append([1, language])

    print(len(languages))
    for i in range(len(languages)):
        for j in range(0, len(languages) - i - 1):
            if(languages[j][0] < languages[j + 1][0]):
                tmp = languages[j]
                languages[j] = languages[j + 1]
                languages[j + 1] = tmp
    return languages[:count]

print(most_spoken_languages('../data/countries_data.json', 10))
print(most_spoken_languages('../data/countries_data.json', 3))

# LEVEL 2

with open('../data/email_exchanges_big.txt') as f:
    text = f.read()
    addresses = re.findall(r'[a-z.]+@[a-z.]+', text, re.I)
print(set(addresses))

with open('../data/hacker_news.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    text = [1, 2, 5]
    counter = 0
    for row in csv_reader:
        for i in text:
            if(len(re.findall(r'\b[Jj]ava\b', row[i])) > 0):
                counter += 1
                break
print(counter)
