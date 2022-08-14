from constants import TARGET_URL
from requests import get
from bs4 import BeautifulSoup
import re

def get_list_of_available_urls():

    available_urls_list = []
    
    html_doc = get_html_doc(TARGET_URL)
    urls_list = html_doc.find_all('a', href=re.compile('ps32'))

    for url in urls_list:
        available_urls_list.append(url.attrs['href'])

    return available_urls_list

def scrape_data(url):
    
    data = []
    tags_tr = get_html_doc(url).find_all('tr')
    
    i = 0
    for tag_tr in tags_tr:
        tag_td = tag_tr.find('td', {'class': 'cislo'})

        if tag_td:
            i = i + 1

            tag_a = tag_td.find('a')
            city_code = tag_a.get_text()
            city_url = tag_a.attrs['href']

            tag_td = tag_tr.find('td', {'class': 'overflow_name'})
            city_name = tag_td.get_text()

            data.append({
                'code': city_code,
                'location': city_name
            })

        if i > 10:
            break

    return data

def get_html_doc(url):

    response = get(url)
    return BeautifulSoup(response.text, features='html.parser')