
import requests as req
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

url = "https://dramakoreaindo.art/"

def extract_data():
    html_code = req.get(url).text
    soup = BeautifulSoup(html_code, 'html.parser')

    data_list = []

    articles = soup.find_all('article', class_='mh-loop-item')
    for article in articles:
        title_elem = article.find('h3', class_='entry-title')
        link_elem = title_elem.find('a')
        img_elem = article.find('img', class_='wp-post-image')

        title = title_elem.text.strip()
        link = link_elem['href']
        img_link = img_elem['data-src'] if img_elem else None
        
        endpoint = urlparse(link).path
        
        data_list.append({'title': title, 'link': link, 'img_link': img_link, 'endpoint': endpoint})

    return data_list

def extract_article_content(link):
    response = req.get(url + link)
    if response.status_code == 200:
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')
        
        content_elem = soup.find('div', id='main-content')
        return content_elem
        # if content_elem:
        #     article_content = content_elem.get_text(strip=True)
        #     return article_content
    return None

# Extract and print the data
# data = extract_data()
# print(data)

# # Example: Extract and print article content for the first item
# if data:
#     first_item_link = data[0]['link']
#     print(first_item_link)
#     article_content = extract_article_content(first_item_link)
#     if article_content:
#         print("\nArticle Content:\n", article_content)
#     else:
#         print("\nFailed to retrieve article content.")

