import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint

def get_data():
    url = 'https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir/posutochnaya-arenda-kvartir/q-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B-%D0%BF%D0%BE-%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE'
    r = requests.get(url, verify=False)    # def get_data()
    soup = BeautifulSoup(r.content, 'html.parser')
    all_ = soup.findAll('div', class_='main-feed__wrapper')
    return all_

def parse_data():
    result = []
    price = []
    image = []
    k = 0
    for item in get_data():
        all_image = item.findAll('img', class_='lazyload')
        all_price = item.findAll('p', class_='adTile-price')
        all_name = item.findAll('a', class_='adTile-title')
        for i in all_image:
            if i['alt'] != 'paid feature icon' and i['alt'] != '':
                image.append(i['data-src'])
        for price_items in all_price:
            price.append(price_items.get_text())
        for items in all_name:
            result.append({
                'Name' : items.get_text().replace('\n', ' '),
                'Link_Name' : 'https://lalafo.kg' + items['href'],
                'Price' : price[k],
                'Link_image' : image[k]
            })
            k += 1
    return result

def save_data():
    with open('result.csv', 'w') as f:   # def save_data()
        writer = csv.DictWriter(f, fieldnames=['Name', 'Link_Name', 'Price', 'Link_image'])
        writer.writeheader()
        writer.writerows(parse_data())

def main():
    save_data()

if __name__ == '__main__':
    main()