    # 메일 발신 고급  : 07 :53:24~~~~
    # 메일 제목, 본문 한글로  보내기

import smtplib
from account import * # 만들어 놓은 이메일과 패스워드 사용하기 위해~~
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일 입니다."# 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "limwanjae@gmail.com" # 받는 사람

# 여러사람에게 메일을 보낼때는~~ 
#  콤마로 구분해서 추가
#msg["To"] = "limwanjae@gmail.com, limwanjae@gmail.com,limwanjae@gmail.com"

# # 또는 
# to_list = [limwanjae@gmail.com, limwanjae@gmail.com,limwanjae@gmail.com]
# msg["To"] = ", ".join(to_list)

# # 참조
# msg["Cc"] = "limwanjae@gmail.com, limwanjae@gmail.com,limwanjae@gmail.com"

# # 비밀참조
# msg["Bcc"] = "limwanjae@gmail.com, limwanjae@gmail.com,limwanjae@gmail.com"

msg.set_content("테스트 본문입니다")# 메일 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls()# 모든 내용이 암호화 되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)# 로그인 수행
    smtp.send_message(msg)

