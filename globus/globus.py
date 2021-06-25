


# import requests # делаем запрос сайту
# from bs4 import BeautifulSoup

# GLOBUS_URL = 'https://globus-online.kg/catalog/konditerskie_izdeliya/'

# def get_html(url):
#     r = requests.get(url)
#     # print(r.status_code)
#     return r.text


    
# html= get_html(GLOBUS_URL)
# with open('/home/kyial/desktop/parsers/globus/globus_page.html', 'w') as file:
#     file.write(html)

# def extract_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_="list-showcase__inner js-element__shadow")
#     # first_item = soup.find('div', class_="list-showcase__inner js-element__shadow")
#     for block in items:
#         # img = block.img['src']
#         # print(img)
#         image_block = block.find("div",class_ = "list-showcase__picture")
#         try:

#             image = image_block.img["data-src"]
#             print("https://globus-online.kg/" + image)
#         except KeyError:
#             print("Картинки нет")
#         # print(img)
#     # print(items.text)
#     # print(type(soup))
# extract_data(html)


### ДЗ #######

# import os
# import psycopg2

# import requests
# from bs4 import BeautifulSoup


# GLOBUS_URL = "https://globus-online.kg/catalog/ovoshchi_frukty_orekhi_zelen/"

# def get_html(url):
#     r = requests.get(url)
#     return r.text
    
# html= get_html(GLOBUS_URL)
# with open('/home/kyial/desktop/parsers/globus/globus_page.html', 'w') as file:
#     file.write(html)

# def extract_data(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     items = soup.find_all('div', class_="list-showcase__inner js-element__shadow")
#     products = []
#     images = []
#     articyls = []
#     prices = []

#     for block in items:
#         image_block = block.find("div",class_ = "list-showcase__picture")
#         try:
#             image = image_block.img["data-src"]
#             link_im = "https://globus-online.kg/" + image
#         except:
#             print("Картинки нет")
#         images.append(link_im)
#         name_block = block.find("div",class_ = "list-showcase__name")
#         name = name_block.a.text
#         products.append(name)
#         price_block = block.find("div", class_ ="list-showcase__prices") 
#         price = price_block.span.text
#         prices.append(int(price.split()[0]))
        

#     for block in items:
#         art_block = block.find("div", class_ ="list-showcase__article")
#         art = art_block.b.text
#         articyls.append(art)
            

# user  = input('Введите название пользователя: ')
# password = input('Введите пароль БД: ')

# db = 'globus'

# try:
#     connection = psycopg2.connect(  
#         dbname=db, 
#         user=user,
#         password=password,
#         host='localhost')

    
# except psycopg2.OperationalError:
#     os.system(f"psql -U {user} -c 'CREATE DATABASE {db};' -W")
#     connection = psycopg2.connect(
#         dbname=db,
#         user=user,
#         password=password,
#         host='localhost')

# cursor = connection.cursor()


# create_table_cmd = '''CREATE TABLE fruits(
#     id SERIAL PRIMARY KEY, 
#     product_name VARCHAR(50), 
#     image VARCHAR, 
#     articyl VARCHAR(50), 
#     price INT
#     );'''
# cmd_1 = '''INSERT INTO fruits(
#     product_name, 
#     image, 
#     articyl,
#     price)VALUES'''

# extract_data(html)
# for k in range(len(products)):
#     cmd_1 +=f'("{products[k]}", "{images[1]}", "{articyls[1]}", {prices[k]}),'

# cmd_1 = cmd_1 + ';'
# cursor.execute(cmd_1)
# connection.commit()
# connection.close()

# cursor.execute(create_table_cmd)
# connection.commit()
##################### ломается###############################

#########################globus.py#########################

# import requests
# from bs4 import BeautifulSoup
# import psycopg2

# class Requster(object):
#     def __init__(self, url):
#         self.url = url
    

#     def get_html(self):
#         r = requests.get(self.url)
#         if r.status_code == 200:
#             return r.text
#         else:
#             return 0

# class Scraper(object):
#     def __init__(self, html):
#         self.soup = BeautifulSoup(html, 'html.parser')


#     def img_finder(self):
#         all_blocks = self.soup.find_all('div', class_ = 'list-showcase__picture')
#         for block in all_blocks:
#             img = block.a.img
#             try:
#                 img_url = img["data-src"]
#                 yield img_url
#             except KeyError:
#                 yield '0'


#     def text_finder(self):
#         all_blocks = self.soup.find_all('div', class_ = 'list-showcase__name')
#         for block in all_blocks:
#             text = block.a.text
#             try:
#                 text_url = text
#                 yield text_url 
#             except KeyError:
#                 yield '0' 


#     def price_finder(self):
#         all_blocks = self.soup.find_all('div', class_="c-prices js-prices view-list page-list product-alone multyprice-no")
#         for block in all_blocks:
#             price = block.span
#             try:
#                 price_url = price["data-price"]
#                 yield price_url 
#             except KeyError:
#                 yield '0' 

    
#     def articl_finder(self):
#         all_blocks = self.soup.find_all('div', class_="list-showcase__article")
#         for block in all_blocks:
#             articl = block.b.text
#             try:
#                 articl_url = articl
#                 yield articl_url 
#             except KeyError:
#                 yield '0' 

        
#     def html_finder(self):
#         all_blocks = self.soup.find_all('div', class_="list-showcase__name")
#         for block in all_blocks:
#             sylka = block.a
#             try:
#                 sylka_url = sylka["href"]
#                 yield sylka_url 
#             except KeyError:
#                 yield '0' 




# r1 = Requster('https://globus-online.kg/catalog/myaso_ptitsa_ryba/')
# html = r1.get_html()
# if html:
#     scraper = Scraper(html)
#     img = scraper.img_finder()
#     texts = scraper.text_finder()
#     prices = scraper.price_finder()
#     articls = scraper.articl_finder()
#     sylka = scraper.html_finder()
# else:
#     raise RuntimeError('Ty lox')


# image = []
# product_name = []
# price = []
# articl = []
# link = []

# for i in img:
#     image.append(i)
# for j in texts:
#     product_name.append(j)
# for x in prices:
#     price.append(x)
# for p in articls:
#     articl.append(p)
# for a in sylka:
#     link.append(a)

# bd_password = input("Введите пароль от Базы Данных: ")


# conn = psycopg2.connect(
#     dbname='postgres', 
#     user='postgres', 
#     password=bd_password, 
#     host='localhost'
# )

# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE globus_html(
#     id SERIAL PRIMARY KEY, image VARCHAR(200) NOT NULL, 
#     product_name VARCHAR(80) NOT NULL, 
#     price VARCHAR(10) NOT NULL, 
#     articl VARCHAR(20) NOT NULL, 
#     link VARCHAR(150) NOT NULL);'''
# )

# query = '''INSERT INTO globus_html(image, product_name, price, articl, link) VALUES '''
# for index in range(len(image)):
#     query += f'(\'{image[index]}\', \'{product_name[index]}\', \'{price[index]}\', \'{articl[index]}\', \'{link[index]}\'),'

# sql_query = query[:-1] + ';'


# cursor.execute(sql_query)
# conn.commit()



# cursor.close()
# conn.close()

