
import requests
from bs4 import BeautifulSoup

url = "https://dramakoreaindo.art/my-lovely-liarrr/"

def extract_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')
        
        content_elem = soup.find('div', id='main-content')
        if content_elem:
            article_content = content_elem.get_text(strip=True)
            return article_content
    return None

article_content = extract_article_content(url)
if article_content:
    print(article_content)
else:
    print("Failed to retrieve article content.")
