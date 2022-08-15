from constants import TARGET_URL, TARGET_URL_BEGIN
from requests import get
from bs4 import BeautifulSoup
import re

def get_list_of_available_urls():

    available_urls_list = []
    
    html_doc = get_html_doc(TARGET_URL)
    urls_list = html_doc.find_all('a', href=re.compile('ps32'))

    for url in urls_list:
        available_urls_list.append(TARGET_URL_BEGIN + url.attrs['href'])

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
            city_url = TARGET_URL_BEGIN + tag_a.attrs['href']

            tag_td = tag_tr.find('td', {'class': 'overflow_name'})
            city_name = tag_td.get_text()

            # Basic info
            city_dict = {
                'code': city_code,
                'location': city_name
            }

            html_doc = get_html_doc(city_url)
            city_dict['registered'] = html_doc.find('td', {'headers': 'sa2'}).get_text()
            city_dict['envelopes'] = html_doc.find('td', {'headers': 'sa3'}).get_text()
            city_dict['valid'] = html_doc.find('td', {'headers': 'sa6'}).get_text()

            # Election results
            tds_tag = html_doc.find_all('td', {'class': ['overflow_name', 'cislo'], 'headers': ['t1sb2', 't1sb3', 't2sb2', 't2sb3']})

            party_name = ''
            for td_tag in tds_tag:

                if 'overflow_name' in td_tag.attrs['class']:
                    party_name = td_tag.get_text() # saving for next iteration
                    continue

                if 'cislo' in td_tag.attrs['class']:
                    city_dict[party_name] = td_tag.get_text()
                    party_name = '' # clearing name

            data.append(city_dict)

        if i > 1:
            # process only few of them (during dev)
            break

    return data

def get_html_doc(url):

    response = get(url)
    return BeautifulSoup(response.text, features='html.parser')