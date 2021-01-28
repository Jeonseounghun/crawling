from os import close
import requests
from bs4 import BeautifulSoup
#########url 추출

####### 홈페이지 화면 상품 추출
url ="https://search.musinsa.com/category/001"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


f = open("data_list.txt", "w", encoding="utf8")

link = soup.find_all("a", {"name":"goods_link"})
for i in link:
    data = i["href"] + "\n"
    f.write(data)
f.close()
