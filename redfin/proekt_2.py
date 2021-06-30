import os
import requests
import psycopg2
from bs4 import BeautifulSoup
import time
import pathlib

SITE_URL = "https://www.redfin.com/city/1826/MA/Boston/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.redfin.com/",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    
}

class Redfin(object):

    def __init__(self, url):
        self.url = url

    def get_html(self, url):
        r = requests.get(url=url, headers = HEADERS)  
        print(r.status_code) 
        if r.status_code == 200:          
            time.sleep(3.5)
            return r.text
        else:
            return 0

    def main_page(self):
        html = self.get_html(self.url)
        # print(html)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pairs_block = soup.find_all("div", id="right-container")
            # print(pairs_block)
            for pair in pairs_block:
                pairs = pair.find_all("div", class_ = "v2 interactive")
                # print(pairs)
                for item in pairs:
                    article_houses = item.a["href"]
                    link_house = "https://www.redfin.com" + article_houses
                    #print(link_house)
                    link_houses_html = self.get_html(link_house)
                    #print(link_houses_html)
                   
                    if link_houses_html:
                        houses_soup = BeautifulSoup(link_houses_html, "html.parser")
                        #print(houses_soup)
                        all_block = houses_soup.find("div", class_ = " landscape")
                        print(all_block)
                        for images in all_block:
                            link_images = images.img["src"]
                            #print(link_images)

                        blocks_beds_bath = houses_soup.find("div", class_ = "Section AddressBannerSectionV2 white-bg not-omdp")
                        #print(blocks_beds_bath)
                        for block1 in blocks_beds_bath:
                            beds = block1.find("div", class_ = "stat-block beds-section").text[0]
                            bath = block1.find("div", class_ = "stat-block baths-section").text[0]
                            #print(bath)

                        blocks_house_info = soup.find_all("div", class_ = "house-info-container")
                        print(blocks_house_info)
                        for block2 in blocks_house_info:
                            price = block2.find("div", class_ = "content text-right").text

                        
                            


                        
                        

       
            # print(pictures_list)

            # print(pairs_block)
        
                
               

            
redfin = Redfin(SITE_URL)
redfin.main_page()

# """ redfin.get_html() """
# try:
#      pages = redfin.get_number_of_pages()
#      for page in range(1, pages - 3):
#          generator = redfin.main_page(page)
# except requests.exceptions.ConnectionError:
#     print("Нет интернета!")
# """ html_page = redfin.get_html(REDFIN_URL)
# with open("./redfin.html", "w") as f:
#     f.write(html_page) """
    
        


        
    # def get_number_of_pages(self):
    #     html = self.get_html(self.url)
    #     if html:
    #         soup = BeautifulSoup(html, "html.parser")
    #         pagination = soup.find("div", class_ = "PagingControls")
    #         number_of_page = pagination.text
    #         print(int(number_of_page[-1]))
    #     #     return int(number_of_page[-1])
    #     # else:
        #     return 0



