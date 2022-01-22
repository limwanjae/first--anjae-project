# 이메일 자동화   07:40:38~~~
# 환경설정 : 구글 g_mail 기준으로 설명
# 구글 이메일에서
#오른쪽 점9개 눌러서~~ 구글계정으로
#구글계정에서 보안 눌러서 2단계 인증하고~~
# 다시 보안에서 앱 비밀번호 설정을 하고~~ 설정한 비빌번호를
# account.py에 구글 이메일과 패스워드를 입력해 놓고서~~~시작~~~

# 메일 보내기 

import smtplib
from account import * # 만들어 놓은 이메일과 패스워드 사용하기 위해~~

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #연결이 잘 수립되는지 확인
    smtp.starttls()# 모든 내용이 암호화 되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)# 로그인 수행

    # 메일 보내기
    subject = "test mail"# 메일 제목
    body = "mail body" # 메일 본문

    # 메시지를 보내기 위해서는 일정한 형태가 있음
    msg = f"Subject: {subject}\n{body}"

    # 발신자, 수신자, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "limwanjae@gmail.com", msg)





