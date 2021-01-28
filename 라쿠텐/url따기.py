from selenium import webdriver
from bs4 import BeautifulSoup
import time
url_list = []


file = open("url.txt", "r", encoding="utf8")
lines = file.readlines()
file.close()
for line in lines:
#### Webdriver 실행
    dr = webdriver.Chrome('./chromedriver.exe') 

    f = open("url모음.txt", "a", encoding="utf8")
    #### Webdriver에서 접속하는 URL
    dr.get('%s' % line)
    html = dr.page_source
    soup2 = BeautifulSoup(html, 'lxml')

    #### 각 상품의 url 추출
    urls = soup2.find_all("a", attrs={"class":"a-link-normal a-text-normal"})

    for url in urls:
        f.write("https://www.amazon.com" + url["href"] + "\n")

    f.close
    dr.quit()