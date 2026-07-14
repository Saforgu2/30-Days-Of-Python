# DAY 22

from bs4 import BeautifulSoup
import requests
import json

# LEVEL 1
'''
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

if(response.status_code == 200):
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.title.get_text())
    
    data = list()
    community_and_academics = soup.find_all('section', class_='stat-section')
    
    for section in community_and_academics:
        element = dict()
        items = section.find_all('li')
        element['category'] = section.find('h4', class_='stat-group-title').text
        
        for item in items:
            label = item.find('span', class_='stat-label').text
            value = item.find('span', class_='stat-figure').text
            element[label] = value

        data.append(element)

    campus_heading = soup.find('h4', string='Campus')
    campus_container = campus_heading.find_next_sibling('div', class_='bu-stat-list bu-stat-count-5')
    campus_articles = campus_container.find_all('article', class_='bu-stat-single')
    
    element = dict()
    element['category'] = campus_heading.text
    
    for article in campus_articles:
        label = article.find('h3', class_='bu-stat-title').text.strip()
        value = article.find('span', class_='bu-stat-value-field').text
        element[label] = value

    data.append(element)
        
    with open('bu_json_file.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
'''
# LEVEL 3

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

print(response.status_code)

if(response.status_code == 200):
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    print(soup.title.get_text())

    h2 = soup.find_all('h2', {'id': 'Presidents'})
    print(h2)

    table = soup.find('table', class_='wikitable')
    print(table)
