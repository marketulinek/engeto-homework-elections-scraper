from constants import TARGET_URL
from requests import get
from bs4 import BeautifulSoup
import re

def get_list_of_available_urls():

    response = get(TARGET_URL)
    available_urls_list = []

    html_doc = BeautifulSoup(response.text, features='html.parser')
    urls_list = html_doc.find_all('a', href=re.compile('ps32'))

    for url in urls_list:
        available_urls_list.append(url.attrs['href'])

    return available_urls_list