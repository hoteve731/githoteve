from unittest import result #이거 제가 쓴 적이 없는데 왜 생기는거죠???
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

results = soup.findAll('p','title') 
openfile = open("practice1.txt",'w', encoding="UTF-8")
openfile.write(str(datetime.now())+"의 벅스 실시간 차트 순위입니다.\n")

for title in results: 
    openfile.write( str(rank)+ "위: "+ str(title.get_text())+"\n") 
    rank = rank + 1


#아래는 삽질의 흔적....
# rank = rank + 1
#     title = titles[i]
#     print(rank,"위: ",result.get_text(),"\n")


# for result in results:
#     musicfile.write(str(rank)+"위: "+result.get_text()+"\n")
#     print(rank,"위: ",result.get_text(),"\n")
#     rank = rank +1 



