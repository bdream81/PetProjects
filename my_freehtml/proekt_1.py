import os
import requests
from bs4 import BeautifulSoup
import psycopg2

SITE_URL = "https://freehtml5.co/"

class Freehtml5(object):
    def __init__(self, url):
        self.url = url

    def get_html(self, url):
        r = requests.get(url)

        if r.status_code == 200:
            return r.text
        else:
            return 0

    
    def main_page(self, page):
        html = self.get_html(f"https://freehtml5.co/page/{page}/")

        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_block = soup.find_all("div", class_="col-sm-12 col-md-6 col-lg-4")

            pictures_link = []
            headers_list = []
            date_list = []
            article_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            downloads_list = []
            views_list = []

            for block in all_block:

                pictures = block.img["src"]
                pictures_link.append(pictures)

                headers = block.div.h2.a.text
                headers_list.append(headers)

                date = block.div.div.p.small.text.replace(",", "").split(" ")[1:4]
                date_list.append("-".join(date))
                article_link = block.a["href"]
                article_definition_html = self.get_html(article_link)      
                if article_definition_html:
                    definition_soup = BeautifulSoup(article_definition_html, "html.parser")
                    text_blocks = definition_soup.find("div", class_ = "entry-content")
                    # for i in text_blocks:
                    #     article_list.append(i.text)

                pairs = block.find("p", class_ ="card-text hits")
                download = pairs.text.strip(" ").split(" ")
                if download[1] == "Downloads":
                    downloads_list.append(int(download[0].replace(",", "")))
                else:
                    downloads_list.append(0)

                item = block.find("p", class_ ="card-text hits")
                views = item.text.strip(" ").split(" ")
                if views[1] == "Views":
                    views_list.append(int(views[0].replace(",", "")))
                else:
                    views_list.append(int(views[2].replace(",", "")))

            yield {"pictures": pictures_link, "header": headers_list, "publication_date": date_list, "text": article_list, "downloads": downloads_list, "views": views_list}
            # print(date_list)
                    
        return "Error!"

    def get_number_of_pages(self):
            html = self.get_html(self.url)
            if html:
                soup = BeautifulSoup(html, "html.parser")
                pagination = soup.find("ul", class_="pagination")
                number_of_pages = pagination.text.split(" ")
                return int(number_of_pages[-2])
            return 0

freehtml = Freehtml5(SITE_URL)
freehtml.get_number_of_pages()

user  = input('Введите название пользователя: ')
password = input('Введите пароль БД: ')

db = 'proekt_1'

try:
    connection = psycopg2.connect(  
        dbname=db, 
        user=user,
        password=password,
        host='localhost')

    
except psycopg2.OperationalError:
    os.system(f"psql -U {user} -c 'CREATE DATABASE {db};' -W")
    connection = psycopg2.connect(
        dbname=db,
        user=user,
        password=password,
        host='localhost')

cursor = connection.cursor()


create_table_cmd = '''CREATE TABLE freehtml5(
    id SERIAL PRIMARY KEY, 
    picture VARCHAR NOT NULL, 
    publication_date VARCHAR(30) NOT NULL, 
    header VARCHAR NOT NULL, 
    definition INT NOT NULL,
    downloads INT NOT NULL,
    views INT NOT NULL
    );'''
cursor.execute(create_table_cmd)
connection.commit()

cmd_1 = '''INSERT INTO freehtml5(picture, publication_date, header, definition, downloads, views) VALUES'''

try:
    pages = freehtml.get_number_of_pages()

    for page in range(1, pages + 1):
        generator = freehtml.main_page(page)
        for sait in generator:
            cmd_1 += f'(\'{sait.get("picture")}\', \'{sait.get("publication_date")}\', \'{sait.get("header")}\', \'{sait.get("definition")}\', \'{sait.get("downloads")}\', \'{sait.get("views")}\'),'
        print(sait.get("publication_date"))   
except requests.exceptions.ConnectionError:
    print("Нет интернета!")

sql_cmd_1 = cmd_1[:-1] + ';'

cursor.execute(sql_cmd_1)
connection.commit()

connection.close()
cursor.close()


































