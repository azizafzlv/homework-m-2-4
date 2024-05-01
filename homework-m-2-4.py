"""
На сайте https://dominopizza.ru/ есть раздел Закуски,
необходимо спарсить данные по каждому продукту
(название, состав, цена, и ссылку на картину):
"""

import requests
from bs4 import BeautifulSoup


base_url = 'https://dominopizza.ru/'
response = requests.get(base_url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

zakuski = soup.find('div', {'id': 'zakuski'}).find_all(
    'div', {'class': 'col'})

zakuski_list = []

for item in zakuski:
    zakuski_content = item.a.div.find('div', {'class': 'product-card-content'})
    zakuski_name = zakuski_content.find('div', {'class': 'product-name'})
    zakuski_descrip = zakuski_content.find('div', {'class': 'description-container'})
    zakuski_price = zakuski_content.find('div', {'class': 'price'})
    zakuski_picture = item.a.div.find('div', {'class': 'product-picture'})


    zakuski_list.append({
        'name': zakuski_name.get_text(),
        'descrip': zakuski_descrip.get_text(),
        'price': zakuski_price.get_text(),
        'picture_url': zakuski_picture.picture.img.get('src')
    })


print('Закуски')
for item in zakuski_list:
    print('*******************************')
    print(f'Наименование: {item["name"]}')
    print(f'Состав: {item["descrip"]}')
    print(f'Цена: {item["price"]}')
    print(f'Ссылка на картинку: {item["picture_url"]}')

