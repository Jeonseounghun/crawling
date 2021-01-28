from os import close
from bs4 import BeautifulSoup
import urllib.request
import requests
f = open("data_list.txt", "r", encoding="utf8")

data_lists = f.readlines()
f.close
i =1
for data_list in data_lists:
    if i%2 ==0 :
        url ="%s" % data_list
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(url).read()
        
        soup = BeautifulSoup(res,'html.parser')
        soup = soup.find("div",{"class":"product-img"})
        #img의 경로를 받아온다
        imgUrl = soup.find("img")["src"]
        
        #urlretrieve는 다운로드 함수
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        res2 = requests.get(url, headers=header)
        res2.raise_for_status()
        soup2 = BeautifulSoup(res2.text, "lxml")
        product = soup2.find("span" , attrs={"class":"product_title"})
        title = product.get_text().strip()[:10]
        
        
        urllib.request.urlretrieve("https:" + imgUrl, "%s" % title+'.jpg')
        print("%s/%s 진행" % (i,len(data_lists)+1))
        i += 1
    else:
        i += 1
        continue
        