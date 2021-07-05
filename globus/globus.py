import os
import psycopg2

import requests
from bs4 import BeautifulSoup


GLOBUS_URL = "https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/"

class Requster(object):
    def __init__(self, url):
        self.url = url

    def get_html(self, url):
        r = requests.get(url=url)  
        
        if r.status_code == 200:          
            return r.text
        else:
            return 0

    
    def images(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_bloks = soup.find_all('div', class_="list-showcase__picture")
            images = []
            for block in all_bloks:
                img = block.img["src"]
                images.append(img)
            return images

    def names(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_bloks = soup.find_all('div', class_="list-showcase__name")
            names = []
            for block in all_bloks:
                name = block.a.text
                names.append(name)
            return names    

    def prices(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_bloks = soup.find_all("span", class_= "c-prices__value js-prices_pdv_ГЛОБУС Розничная")
            prices = []
            for block in all_bloks:
                price = block.text.split()[0]
                prices.append(price)
            return prices              
                
    def articles(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_bloks = soup.find_all("div", class_= "list-showcase__article")
            articles = []
            for block in all_bloks:
                article = block.b.text
                articles.append(article)
            return articles               
                    
    def links(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_bloks = soup.find_all("div", class_= "list-showcase__picture")
            links = []
            for block in all_bloks:
                link = block.a["href"]
                links.append("https://globus-online.kg" + link)
            return links

r = Requster(GLOBUS_URL) 
i = r.images()     
n = r.names()
p = r.prices()
a= r.articles()
l = r.links()

bd_password = input("Введите пароль от Базы Данных: ")


conn = psycopg2.connect(
    dbname='globus', 
    user='postgres', 
    password=bd_password, 
    host='localhost'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE globus2(
    id SERIAL PRIMARY KEY, 
    product_name VARCHAR(200) NOT NULL, 
    images VARCHAR NOT NULL, 
    price VARCHAR(10) NOT NULL,
    article VARCHAR(50),
    link VARCHAR);'''
)

conn.commit()
query1 = '''INSERT INTO globus2(product_name, images, price, article, link) VALUES '''

for indx in range(len(n)):
    query1 += f'(\'{n[indx]}\', \'{i[indx]}\', \'{p[indx]}\', \'{a[indx]}\', \'{l[indx]}\'),'
    
sql_query1 = query1[:-1] + ';'
cursor.execute(sql_query1)
conn.commit()

cursor.close()
conn.close()
