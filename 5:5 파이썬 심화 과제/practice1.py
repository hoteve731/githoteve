from unittest import result #이거 제가 쓴 적이 없는데 왜 생기는거죠???
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('p.title') #p 태그 안에 또 a태그로 들어있어서 a태그 써야하는줄 알고 삽질했습니다...ㅠㅠ

print(datetime.today().strftime("%Y년 %m월 %d일의 벅스 실시간 차트 순위입니다.\n"))

rank = 1

for i in range(0,20): #리스트 길이만큼 할수도 있지만 너무 길어져서 20위로 잘랐어요
    print(rank, "위: ",titles[i].text) #아직도 이렇게 간단하게 되네? 라고 믿기지가 않는 코드
    rank = rank + 1


#아래는 삽질의 흔적....
# rank = rank + 1
#     title = titles[i]
#     print(rank,"위: ",result.get_text(),"\n")


# for result in results:
#     musicfile.write(str(rank)+"위: "+result.get_text()+"\n")
#     print(rank,"위: ",result.get_text(),"\n")
#     rank = rank +1 



