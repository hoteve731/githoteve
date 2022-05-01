from unittest import result
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('p.title')

print(datetime.today().strftime("%Y년 %m월 %d일의 벅스 실시간 차트 순위입니다.\n"))
rank = 1

for i in range(0,20):
    print(rank, "위: ",titles[i].text)
    rank = rank + 1


# rank = rank + 1
#     title = titles[i]
#     print(rank,"위: ",result.get_text(),"\n")


# for result in results:
#     musicfile.write(str(rank)+"위: "+result.get_text()+"\n")
#     print(rank,"위: ",result.get_text(),"\n")
#     rank = rank +1 



