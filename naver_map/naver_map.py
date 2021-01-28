from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from openpyxl.styles import PatternFill, Color
from openpyxl import Workbook
import datetime
import requests
from urllib3 import request

list_2 = [1,2,3,4,4]
place_list = []

f = open("리스트.txt", "r", encoding="utf8")
place_list = f.readlines()
f.close()
for place in place_list:
    file = open(place.strip() + ".txt", "a", encoding="utf8")
    driver = webdriver.Chrome('./chromedriver.exe') 
    driver.get('https://pcmap.place.naver.com/restaurant/list?query={}맛집&x=126.62966251373292&y=37.476603562323426&bounds=126.61906242370607%3B37.46843778341404%3B126.65017604827882%3B37.48459817900955&ts=1610066411630#'.format(place))


    cnt =1
    for i in list_2:
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')




        list = soup.find_all("li", attrs={"class":"_3t81n _1l5Ut"})
        for info in list:
            try:
                place_name = info.find("span", attrs={"class":"_3Yilt"}).get_text()
                
                place_review_2 = info.find_all("span", attrs={"class":"_3Yzhl"})
                
                info = ("%s." % cnt + place_name + "\n")
                file.write(info)
                for a in place_review_2:
                   a = a.get_text()+ "\n"
                   file.write(a)
                b = "-"*100+ "\n"
                file.write(b)
                cnt += 1
            except:
                print("리뷰없음")
        body = driver.find_element_by_xpath('//*[@id="app-root"]/div/div[2]/div[2]/a[%s]' % (i+2))
        body.click()        
        time.sleep(5)
    file.close()
    
   
    driver.quit()