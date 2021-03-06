# import os
import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import psycopg2

SITE_URL = "https://mypizza.kg/"
# os.system(f"wget -r -k -l 7 -p -E -nc {SITE_URL}")

class Pizza(object):

    def __init__(self, url):
        self.url = url
        self.PATH = str(Path(__file__).parent)
    def get_html(self, url):
        r = requests.get(url=url)  
        
        if r.status_code == 200:          
            return r.text
        else:
            return 0

    def zavtrak(self):
        
    
        with open("/home/kyial/desktop/parsers/mypizza.kg/Menu/Category/4354.html", "r") as menu:

            zavtrak_link = menu.read()

            indx1 = zavtrak_link.find("categoryController.init")
            indx2 = zavtrak_link.find("function isNumberKey(evt)")
            all_breakfast_line = zavtrak_link[indx1+len("categoryController.init")+1:indx2].replace("\n", "")
            indx3 = all_breakfast_line.find("document")
            all_breakfast_info =all_breakfast_line[0:indx3-17]

            breakfast_dict = json.loads(all_breakfast_info)

            zavtrak_list = []
            image_zavtrak_list = []
            price_zavtrak_list = []
            
            count = 1
            for bluda in breakfast_dict:
                name_bluda = bluda.get("Name")
                zavtrak_list.append(name_bluda)

                image_zavtrak_link = bluda.get("PicturePath")
                r1 = requests.get(image_zavtrak_link).content
                with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/zavtrak/{count}.jpg", 'wb') as f:
                    f.write(r1)
                image_zavtrak_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/zavtrak/{count}.jpg")
                
                price_zavtrak = bluda.get("Price")
                price_zavtrak_list.append(price_zavtrak)
                count += 1
        return zavtrak_list, image_zavtrak_list, price_zavtrak_list

    def pizza40(self):

        with open("/home/kyial/desktop/parsers/mypizza.kg/Menu/Category/4372.html", "r") as menu:

            pizza40_link = menu.read()

            indx1 = pizza40_link.find("categoryController.init")
            indx2 = pizza40_link.find("function isNumberKey(evt)")
            all_pizza40_line = pizza40_link[indx1+len("categoryController.init")+1:indx2].replace("\n", "")
            indx3 = all_pizza40_line.find("document")
            all_pizza40_info =all_pizza40_line[0:indx3-17]

            pizza40_dict = json.loads(all_pizza40_info)

            pizza40_list = []
            image_pizza40_list = []
            price_pizza40_list = []
            count = 1
            for pizza in pizza40_dict:
                name_pizza = pizza.get("Name")
                pizza40_list.append(name_pizza)

                image_pizza_link = pizza.get("PicturePath")
                r2 = requests.get(image_pizza_link).content
                with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/pizza/{count}.jpg", "wb") as f:
                    f.write(r2)
                image_pizza40_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/pizza/{count}.jpg")

                price_pizza40 = pizza.get("Price")
                price_pizza40_list.append(price_pizza40)
                count += 1
        return pizza40_list, image_pizza40_list, price_pizza40_list
                
    def rolly(self):

        with open("/home/kyial/desktop/parsers/mypizza.kg/Menu/Category/4365.html", "r") as menu:

            rolly_link = menu.read()

            indx1 = rolly_link.find("categoryController.init")
            indx2 = rolly_link.find("function isNumberKey(evt)")
            all_rolly_line = rolly_link[indx1+len("categoryController.init")+1:indx2].replace("\n", "")
            indx3 = all_rolly_line.find("document")
            all_rolly_info =all_rolly_line[0:indx3-17]

            rolly_dict = json.loads(all_rolly_info)

            rolly_list = []
            image_rolly_list = []
            price_rolly_list = []
            count = 1
            for rolly in rolly_dict:
                name_rolly = rolly.get("Name")
                rolly_list.append(name_rolly)

                image_rolly_link = rolly.get("PicturePath")
                r3 = requests.get(image_rolly_link).content 
                with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/rolly/{count}.jpg", "wb") as f:
                    f.write(r3)
                image_rolly_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/rolly/{count}.jpg")

                price_rolly = rolly.get("Price")
                price_rolly_list.append(price_rolly)
                count += 1
        return rolly_list, image_rolly_list, price_rolly_list
                
    def salaty(self):

        with open("/home/kyial/desktop/parsers/mypizza.kg/Menu/Category/4358.html", "r") as menu:

            salaty_link = menu.read()

            indx1 = salaty_link.find("categoryController.init")
            indx2 = salaty_link.find("function isNumberKey(evt)")
            all_salaty_line = salaty_link[indx1+len("categoryController.init")+1:indx2].replace("\n", "")
            indx3 = all_salaty_line.find("document")
            all_salaty_info =all_salaty_line[0:indx3-17]

            salaty_dict = json.loads(all_salaty_info)

            salaty_list = []
            image_salaty_list = []
            price_salaty_list = []

            for salaty in salaty_dict:
                name_salaty = salaty.get("Name")
                salaty_list.append(name_salaty)
            count = 1   
            for salaty in salaty_dict:
                image_salaty = salaty.get("PicturePath")
                r4 = requests.get(image_salaty).content
                with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/salaty/{count}.jpg","wb") as f:
                    f.write(r4)
                image_salaty_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/salaty/{count}.jpg")

                price_salaty = salaty.get("Price")
                price_salaty_list.append(price_salaty)
                count += 1
        return salaty_list, image_salaty_list, price_salaty_list
                
    def zakuski(self):

        with open("/home/kyial/desktop/parsers/mypizza.kg/Menu/Category/4356.html", "r") as menu:

            zakuski_link = menu.read()

            indx1 = zakuski_link.find("categoryController.init")
            indx2 = zakuski_link.find("function isNumberKey(evt)")
            all_zakuski_line = zakuski_link[indx1+len("categoryController.init")+1:indx2].replace("\n", "")
            indx3 = all_zakuski_line.find("document")
            all_zakuski_info =all_zakuski_line[0:indx3-17]

            zakuski_dict = json.loads(all_zakuski_info)

            zakuski_list = []
            image_zakuski_list = []
            price_zakuski_list = []
            count = 1
            for zakuski in zakuski_dict:
                name_zakuski = zakuski.get("Name")
                zakuski_list.append(name_zakuski)

                image_zakuski_link = zakuski.get("PicturePath")
                r5 = requests.get(image_zakuski_link).content
                with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/zakuski/{count}.jpg", "wb") as f:
                    f.write(r5)
                image_zakuski_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/zakuski/{count}.jpg")

                price_zakuski = zakuski.get("Price")
                price_zakuski_list.append(price_zakuski)
                count += 1
        return zakuski_list, image_zakuski_list, price_zakuski_list       
                
    def aksii(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")

            aksya_link = self.get_html("https://mypizza.kg/Shares")
            if aksya_link:
                aksya_soup = BeautifulSoup(aksya_link, "html.parser")
                aksii = aksya_soup.find_all("div", class_ = "c-acticle__content clearfix")

                aksya_list = []
                aksya_img_list = []
                opisanie_aksii_list = []
                count = 1
                for aksya in aksii:
                    aksya_list.append(aksya.text.strip())

                    aksya_img_link = aksya.img["src"]
                    r6 = requests.get(aksya_img_link).content
                    with open(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/aksii/{count}.jpg", "wb") as f:
                        f.write(r6)
                    aksya_img_list.append(f"/home/kyial/desktop/parsers/my_projects/proekt_3/images/aksii/{count}.jpg")
                    count += 1

                aksii_opisanie = aksya_soup.find_all("div", class_ = "c-article__meta")
                for opisanie_link in aksii_opisanie:
                    aksii_opisanie_link = "https://mypizza.kg" + opisanie_link.a["href"]
                    aksii_get = self.get_html(aksii_opisanie_link)
                    
                    aksii_opisanie_link_soup = BeautifulSoup(aksii_get, "html.parser")
                    opisanii = aksii_opisanie_link_soup.find_all("div", class_ ="c-content__text")


                    for opisanie in opisanii:
                        aksia_opisanie = opisanie.text.strip()
                        opisanie_aksii_list.append(aksia_opisanie)
                    
            return aksya_list, aksya_img_list, opisanie_aksii_list
                        
    def vacancy(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")

            vacancy_link = self.get_html("https://mypizza.kg/Vacancies") 
            if vacancy_link:
                vacancy_soup = BeautifulSoup(vacancy_link, "html.parser")
                
                vacancies = vacancy_soup.find_all("div", class_ = "c-vacancy__title")

                vacancy_list = []
                for vacancy in vacancies:
                    vacancy_list.append(vacancy.text.strip())

                

                vac = vacancy_soup.find_all("div", class_ ="c-vacancy__item")

                vac_list =[]
                opisanie_vac_list = []
                for i in vac:
                    vacancii = i.a.text
                    vac_list.append(vacancii)
                    vac_link = i.a["href"]

                    vac_opisanie_link = "https://mypizza.kg" + vac_link
                    vac_get = self.get_html(vac_opisanie_link)
                    
                    vac_opisanie_link_soup = BeautifulSoup(vac_get, "html.parser")
                    opisanii_v = vac_opisanie_link_soup.find_all("div", class_ ="c-content__text")
                  
                    for opisanie in opisanii_v:
                        vacancia_opisanie = opisanie.text.strip()
                        opisanie_vac_list.append(vacancia_opisanie)

            return vac_list, opisanie_vac_list
                 
    def company(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
        
            company_link = self.get_html("https://mypizza.kg/Company/About") 
            if company_link:
                company_soup = BeautifulSoup(company_link, "html.parser")
                company = company_soup.find_all("div", class_ = "c-content__text")

                for company_text in company:
                    company_opisanie = company_text.text
                                     
        return company_opisanie


pizza = Pizza(SITE_URL)
z = pizza.zavtrak()
p = pizza.pizza40()
r = pizza.rolly()
s = pizza.salaty()
zak = pizza.zakuski()
a = pizza.aksii()
v = pizza.vacancy()
c = pizza.company()


bd_password = input("?????????????? ???????????? ???? ???????? ????????????: ")


conn = psycopg2.connect(
    dbname='my_pizzy', 
    user='postgres', 
    password=bd_password, 
    host='localhost'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Zavtrak(
    id SERIAL PRIMARY KEY, 
    nazvanie VARCHAR(200) NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    price TEXT NOT NULL);'''
)
conn.commit()
query1 = '''INSERT INTO Zavtrak(nazvanie, put_do_photo, price) VALUES '''

for j in range(len(z[0])):
    query1 += f'(\'{z[0][j]}\', \'{z[1][j]}\', \'{z[2][j]}\'),'
sql_query1 = query1[:-1] + ';'
cursor.execute(sql_query1)
conn.commit()
    
cursor.execute('''CREATE TABLE Pizza40(
    id SERIAL PRIMARY KEY, 
    nazvanie VARCHAR(200) NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    price TEXT NOT NULL);'''
)
conn.commit()
query2 = '''INSERT INTO Pizza40(nazvanie, put_do_photo, price) VALUES '''

for j in range(len(p[0])):
    query2 += f'(\'{p[0][j]}\', \'{p[1][j]}\', \'{p[2][j]}\'),'

sql_query2 = query2[:-1] + ';'
cursor.execute(sql_query2)
conn.commit()


cursor.execute('''CREATE TABLE Rolly(
    id SERIAL PRIMARY KEY,  
    nazvanie VARCHAR(200) NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    price TEXT NOT NULL);'''
)
conn.commit()
query3 = '''INSERT INTO Rolly(nazvanie, put_do_photo, price) VALUES '''

for j in range(len(r[0])):
    query3 += f'(\'{r[0][j]}\', \'{r[1][j]}\', \'{r[2][j]}\'),'

sql_query3 = query3[:-1] + ';'
cursor.execute(sql_query3)
conn.commit()


cursor.execute('''CREATE TABLE Salaty(
    id SERIAL PRIMARY KEY,  
    nazvanie VARCHAR(200) NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    price TEXT NOT NULL);'''
)
conn.commit()
query4 = '''INSERT INTO Salaty(nazvanie, put_do_photo, price) VALUES '''

for j in range(len(s[0])):
    query4 += f'(\'{s[0][j]}\', \'{s[1][j]}\', \'{s[2][j]}\'),'

sql_query4 = query4[:-1] + ';'
cursor.execute(sql_query4)
conn.commit()

cursor.execute('''CREATE TABLE Zakuski(
    id SERIAL PRIMARY KEY, 
    nazvanie VARCHAR(200) NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    price TEXT NOT NULL);'''
)
conn.commit()
query5 = '''INSERT INTO Zakuski(nazvanie, put_do_photo, price) VALUES '''

for j in range(len(zak[0])):
    query5 += f'(\'{zak[0][j]}\', \'{zak[1][j]}\', \'{zak[2][j]}\'),'

sql_query5 = query5[:-1] + ';'
cursor.execute(sql_query5)
conn.commit()


cursor.execute('''CREATE TABLE Aksii(
    id SERIAL PRIMARY KEY, 
    nazvanie VARCHAR NOT NULL, 
    put_do_photo VARCHAR NOT NULL, 
    opisanie TEXT NOT NULL);'''
)
conn.commit()
query6 = '''INSERT INTO Aksii(nazvanie, put_do_photo, opisanie) VALUES '''

for j in range(len(a[0])):
    query6 += f'(\'{a[0][j]}\', \'{a[1][j]}\', \'{a[2][j]}\'),'
sql_query6 = query6[:-1] + ';'
cursor.execute(sql_query6)
conn.commit()



cursor.execute('''CREATE TABLE Vacancy(
    id SERIAL PRIMARY KEY, 
    nazvanie VARCHAR(200) NOT NULL, 
    opisanie TEXT NOT NULL);'''
)
conn.commit()

query7 = '''INSERT INTO Vacancy(nazvanie, opisanie) VALUES '''
for j in range(len(v[0])):
    query7 += f'(\'{v[0][j]}\', \'{v[1][j]}\'),'

sql_query7 = query7[:-1] + ';'
cursor.execute(sql_query7)
conn.commit()


cursor.execute('''CREATE TABLE O_nas(
    id SERIAL PRIMARY KEY, 
    opisanie TEXT NOT NULL);'''
)
conn.commit()

query8 = '''INSERT INTO O_nas(opisanie) VALUES '''
query8 += f'(\'{c}\'),'

sql_query8 = query8[:-1] + ';'
cursor.execute(sql_query8)
conn.commit()


cursor.close()
conn.close()












