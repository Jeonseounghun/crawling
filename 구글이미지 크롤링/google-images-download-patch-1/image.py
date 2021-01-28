from google_images_download import google_images_download
 
import ssl  # ssl Error 발생 시
ssl._create_default_https_context = ssl._create_unverified_context  
 
 
def imageCrawling(keyword, dir):
    response = google_images_download.googleimagesdownload()
 
    arguments = {"keywords":keyword,      # 검색 키워드
                 "limit":5,             # 크롤링 이미지 수
                 "print_urls":True,       # 이미지 url 출력
                 "no_directory":True,     # 
                 'output_directory':dir}  # 크롤링 이미지를 저장할 폴더
 
    paths = response.download(arguments)
    print(paths)
 


f = open("C:/Users/hp/Desktop/할미새사촌/사료리스트.txt", "r", encoding="utf8")
i = 963
line = f.readlines()
for a in line:
    a = a.strip()
    imageCrawling('%s' % a,'C:/Users/hp/Desktop/할미새사촌/사료/%s-%s' % (i,a))
    i += 1

f.close()
