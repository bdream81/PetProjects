# import os
# import requests
# from bs4 import BeautifulSoup
# import psycopg2

# SITE_URL = "https://freehtml5.co/"

# class Freehtml5(object):
#     def __init__(self, url):
#         self.url = url

#     def get_html(self, url):
#         r = requests.get(url)

#         if r.status_code == 200:
#             return r.text
#         else:
#             return 0

#     def main_page(self, page):
#         html = self.get_html(f"https://freehtml5.co/page/{page}/")

#         if html:
#             soup = BeautifulSoup(html, "html.parser")
#             pairs_block = soup.find_all("main", class_="site-main card-deck row")

#             description = soup.find_all("a", class_ = "btn btn-primary")
#             for zips_articel_teg in description:
#                 zips_articel_teg = description.find("div", class_ = 'single-demo-download')
#                 for zips_articel_item in zips_articel_teg:
#                     zips_articel = zips_articel_item.a["href"]
#                     zips_articel_result = zips_articel.replace("/preview", "/download")
#                     print(zips_articel_result)
#                     os.system(f'wget {zips_articel_result}')

#             for pair in pairs_block:
#                 pairs = pair.find_all("div", class_="col-sm-12 col-md-6 col-lg-4")
                
#                 for item in pairs:
#                     picture = item.img["src"]
#                     header = item.div.h2.a.text
#                     publication_date = item.div.div.p.small.text.replace(",", "").split(" ")[1:4]

                    
#                     downloads_views_block = item.find_all("p",class_ = "card-text hits")
#                     downloads = ""
#                     views = ""
#                     for downloads_views_item in downloads_views_block:
#                         downloads_viwes = downloads_views_item.small.text
#                         downloads_viw = downloads_viwes.split(" ")[1:5]
                        

#                         if len(downloads_viw) < 4:
#                             downloads_viw.insert(0, 'Downloads')
#                             downloads_viw.insert(0, '0')
#                             downloads = downloads_viw[0].replace(",", "")
#                             views = downloads_viw[2].replace(",", "")
                    

#                     article_link = item.a["href"]
#                     article_definition_html = self.get_html(article_link)      
#                     if article_definition_html:
#                         definition_soup = BeautifulSoup(article_definition_html, "html.parser")
#                         text_blocks = definition_soup.find("div", class_ = "entry-content")
#                         text_p = text_blocks.p.text
#                         text_h2 = text_blocks.h2.text

#                         if text_h2 == "Features":

#                             text_li = text_blocks.ul.text
#                             text_f = f'{text_p}\n {text_h2} \n{text_li}'
#                             dict_data = {"picture": picture, "publication_date": publication_date,"header": header, "definition": text_f, "downloads": downloads, "views": views}
#                         yield dict_data

#                     else:
#                         continue

#             return "Ошибка на сайте"

#     def get_number_of_pages(self):
#         html = self.get_html(self.url)

#         if html:
#             soup = BeautifulSoup(html, "html.parser")
#             pagination = soup.find("ul", class_ = "pagination")
#             max_page = pagination.find_all("li", class_ = "page-item")[-2].text.strip()
            
#             return int(max_page)
#         return 0

# freehtml = Freehtml5(SITE_URL)


# user  = input('Введите название пользователя: ')
# password = input('Введите пароль БД: ')

# db = 'proekt_1'

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


# create_table_cmd = '''CREATE TABLE freehtml5(
#     id SERIAL PRIMARY KEY, 
#     picture VARCHAR NOT NULL, 
#     publication_date VARCHAR(30) NOT NULL, 
#     header VARCHAR(50) NOT NULL, 
#     definition TEXT NOT NULL,
#     downloads INT NOT NULL,
#     views INT NOT NULL
#     );'''

# cmd_1 = '''INSERT INTO freehtml5(id, picture, publication_date, header, definition, downloads, views) VALUES'''



# try:
#     pages = freehtml.get_number_of_pages()

#     for page in range(1, pages + 1):
#         generator = freehtml.main_page(page)
#         for sait in generator:
#             cmd_1 += f'(\'{sait.get("picture")}\', \'{sait.get("publication_date")}\', \'{sait.get("header")}\', \'{sait.get("definition")}\', \'{sait.get("downloads")}\', \'{sait.get("views")}\'),'
#             # print(sait)
# except requests.exceptions.ConnectionError:
#     print("Нет интернета!")


# sql_cmd_1 = cmd_1[:-1] + ';'
# print(sql_cmd_1)

# cursor.execute(create_table_cmd)
# connection.commit()

# cursor.execute(sql_cmd_1)
# connection.commit()
# connection.close()

































# # import requests
# # from bs4 import BeautifulSoup
# # import psycopg2

# # SITE_URL = "https://freehtml5.co/"

# # class Freehtml5(object):
# #     def __init__(self, url):
# #         self.url = url

# #     def get_html(self, url):
# #         r = requests.get(url)

# #         if r.status_code == 200:
# #             return r.text
# #         else:
# #             return 0

# #     def main_page(self):
# #         html = self.get_html(f"https://freehtml5.co/page/{page}/")
       
# #         if html:
# #             soup = BeautifulSoup(html, "html.parser")
# #             pairs_block = soup.find_all("main", class_="site-main card-deck row")

# #             for pair in pairs_block:
# #                 pairs = pair.find_all("div", class_="col-sm-12 col-md-6 col-lg-4")
                
# #                 for item in pairs:
# #                     picture = item.img["src"]
# #                     header = item.div.h2.a.text
# #                     publication_date = item.div.div.p.small.text.replace(",", "").split(" ")[1:4]

                    
# #                     downloads_views_block = item.find_all("p",class_ = "card-text hits")
# #                     for downloads_views_item in downloads_views_block:
# #                         downloads_viwes = downloads_views_item.small.text
# #                         downloads_viw = downloads_viwes.split(" ")[1:5]
                        
# #                         if len(downloads_viw) < 4:
# #                             downloads_viw.insert(0, 'Downloads')
# #                             downloads_viw.insert(0, '0')
# #                             downloads = downloads_viw[0].replace(",", "")
# #                             views = downloads_viw[2].replace(",", "")

# #                     article_link = item.a["href"]
# #                     article_definition_html = self.get_html(article_link)      
# #                     if article_definition_html:
# #                         definition_soup = BeautifulSoup(article_definition_html, "html.parser")
# #                         text_blocks = definition_soup.find("div", class_ = "entry-content")
# #                         text_p = text_blocks.p.text
# #                         text_h2 = text_blocks.h2.text

# #                         if text_h2 == "Features":

# #                             text_li = text_blocks.ul.text
# #                             text_f = f'{text_h2} \n{text_li}'
                            
# #                         yield {"picture": picture, "publication_date": publication_date,"header": header, "definition": text_f, "downloads": downloads, "views": views}

# #                     else:
# #                         continue

# #             return "Ошибка на сайте"

# #     def get_number_of_pages(self):
# #         html = self.get_html(self.url)

# #         if html:
# #             soup = BeautifulSoup(html, "html.parser")
# #             pagination = soup.find("ul", class_ = "pagination ")
# #             # pagination_list = pagination.span.text
# #             t = pagination.a.text
# #             number_of_pages = int("".join([i for i in t if i.isdigit()]))
            
# #             print(number_of_pages)

# #             return page
# #         return 0

# # freehtml = Freehtml5(SITE_URL)



# # try:
# #     pages = freehtml.get_number_of_pages()

# #     for page in range(1, pages + 1):
# #         generator = freehtml.main_page(page)
# # except requests.exceptions.ConnectionError:
# #     print("Нет интернета!")


# # # html_page = freehtml.main_page()
# # # with open("./freehtml.html", "w") as f:
# # #     f.write(html_page)






# # picture = []
# # publication_date = []
# # header = []
# # definition = []
# # downloads = []
# # views = []


##################Akjol############

import os
import psycopg2
import requests
from bs4 import BeautifulSoup

SITE_URL = "https://freehtml5.co/"



class Freehtml(object):
    def __init__(self, url):
        self.url = url
    
    def get_html(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return 0
        
    def main_paige(self, page):
        html = self.get_html(f"https://freehtml5.co/page/{page}/")
        
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pairs_block = soup.find_all("main", class_ = "site-main card-deck row")
            
            for pair in pairs_block:

                pairs = pair.find_all("div", "col-sm-12 col-md-6 col-lg-4")
                pictures = ""
                header = ""
                publication_date = ""
                downloads = list()
                views = list()
                for item in pairs:
                    pictures = "".join(item.img["src"])
                    header = "".join(item.div.h2.a.text)
                    publication_date = "".join(item.div.div.p.small.text.replace(",", "").split(" ")[1:4])
                    downloads_views_block = item.find_all("p", class_ = "card-text hits")
                    downloads = ""
                    views = ""
                    for downloads_views_item in downloads_views_block:
                        downloads_views_info = downloads_views_item.small.text
                        downloads_views = downloads_views_info.split("Downloads")
                        if len(downloads_views) == 2:
                            d_and_v = downloads_views[0].replace(" ", "").replace(",", ""), downloads_views[1].split(" ")[1].replace(",", "")
                            downloads = d_and_v[0]
                            views = d_and_v[-1]
                        else:
                            d_v = 0, downloads_views[0].split()[0].replace(",", "")
                            downloads = d_v[0]
                            views = d_v[-1]
                    article_link_description = item.a["href"]
                    article_definition_html = self.get_html(article_link_description)
                    text = ""
                    if article_definition_html:
                        definition_soup = BeautifulSoup(article_definition_html, "html.parser")
                        text_blocks = definition_soup.find_all("div", class_ = "entry-content")
                        for description in text_blocks:
                            before_index = description.text.index('Leave your vote')
                            text = "".join(description.text[0:before_index])
                        article_zips_link = item.a["href"]
                        zips_definition_link = self.get_html(article_zips_link)
                        if zips_definition_link:
                            zips_definition_soup = BeautifulSoup(article_zips_link, "html.parser")
                            zips_definition_button = zips_definition_soup.find_all("ul", class_ = "demo-buttons desktop-only")
                            print(zips_definition_button.a.text)
                        else:
                            continue
                    else:
                        continue
                yield {"pictures": pictures, "header": header, "downloads": downloads, "views": views, "text": text, "publication_date": publication_date}
                   
        return "Oshibka"

    def get_number_of_pages(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.find("ul", class_="pagination")
            number_of_pages = pagination.text.split(" ")
           
            return number_of_pages[-2]
        return 0
freehtml = Freehtml(SITE_URL)
freehtml.get_number_of_pages()

try:
    pages = freehtml.get_number_of_pages()
    for page in range(int(pages)):
        a = freehtml.main_paige(page)
        for i in a:
            image = i.get("pictures")
            header = i.get("header")
            downloads = i.get("downloads")
            publication_date = i.get("publication_date")
            views = i.get("views")
            text = i.get("text")
            print(image)
except requests.exceptions.ConnectionError:
    print("Нет интернета!")



bd_password = input("Введите пароль от Базы Данных: ")

conn = psycopg2.connect(
    dbname='postgres', 
    user='postgres', 
    password=bd_password, 
    host='localhost'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE freehtml(
    id SERIAL PRIMARY KEY, 
    image VARCHAR(200) NOT NULL, 
    header VARCHAR(80) NOT NULL, 
    downloads INT, 
    views INT, 
    text VARCHAR(250) NOT NULL);'''
)

query = '''INSERT INTO freehtml(image, header, downloads, views, text) VALUES '''
for index in range(len(image)):
    query += f'(\'{image[index]}\', \'{header[index]}\', \'{downloads[index]}\', \'{views[index]}\', \'{text[index]}\'),'

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
conn.commit()

cursor.close()
conn.close() 