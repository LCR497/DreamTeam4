from bs4 import BeautifulSoup
import requests

def get_data():
    url = 'https://www.kivano.kg/noutbuki?brands=acer&filter=2-15-53'
    r = requests.get(url, verify=False)    # def get_data()
    soup = BeautifulSoup(r.content, 'html.parser')
    all_ = soup.findAll('div', class_='list-view')
    print(all_)

get_data()