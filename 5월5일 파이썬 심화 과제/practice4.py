import smtplib #설치 필요없는 내장 함수
from email.message import EmailMessage

SMTP_SEVER = "smtp.gmail.com"
SMTP_PORT = 465 #지메일 지정 포트, 변경 불가

message = EmailMessage() #이메일메시지라는 기능이 알아서 MINE으로 변환해 이메일을 담는 통을 만들어 '메시지' 변수에 담아줌
message.set_content("안녕하세요 10기 류호산입니다. 구글은 되는거 확인했는데 받는 대상은 네이버여도 되는건가요?")#본문을 집어넣는 함수

message["Subject"] = '안녕하세요 10기 류호산입니다.'
message["From"] = "fbghtks1000@gmail.com"
message['To'] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SEVER,SMTP_PORT)#원하는 메일'서버에 연결'할 수 있게 해줌
smtp.login("fbghtks1000@gmail.com","fbghtks731!")
smtp.send_message(message)
smtp.quit() #보낸 이후에 서버 연결을 끊음