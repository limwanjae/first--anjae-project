# 파일첨부과 함께 메일 보내는 방법 : 08:01:13~~

import smtplib
from account import * # 만들어 놓은 이메일과 패스워드 사용하기 위해~~
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일 입니다."# 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "limwanjae@gmail.com" # 받는 사람

msg.set_content("다운로드 하세요")# 메일 본문

#MINE TYPE
#msg.add_attachment()
with open("btn_brush.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls()# 모든 내용이 암호화 되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)# 로그인 수행
    smtp.send_message(msg)


