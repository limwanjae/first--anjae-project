# [신청 메일 양식]
# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리(random)
#   (예) 나도코딩/1234

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls()# 모든 내용이 암호화 되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)# 로그인 수행

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "limwanjae@gmail.com" 

        #content = nickname + "/" + str(randint(1000, 9999))
        content = "/".join([nickname, str(randint(1000, 9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 메일 발송 완료") # 8:49:43~~~



