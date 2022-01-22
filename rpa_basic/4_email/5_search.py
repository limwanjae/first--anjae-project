# 메일검색1: 메일 찾아보는 방법 08:23:02~~
# 특정인이 보낸 메일을 검색~~

from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# ~~~
# mailbox.logout()

# 메일박스 객체를 만들고
with  MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:

# ()전체 메일 다 가져오기, limit=5 5개, 최근순으로
# for msg in mailbox.fetch(limit=5, reverse=True):
#     print("[{}] {}".format(msg.from_, msg.subject))
    
# 읽지 않은 메일 가져오기
# for msg in mailbox.fetch('(UNSEEN)'):
#     print("[{}] {}".format(msg.from_, msg.subject))

# # 특정인이 보낸 메일 가져오기
# for msg in mailbox.fetch('(FROM limwanjae@gmail.com)',limit=3, reverse=True):
#     print("[{}] {}".format(msg.from_, msg.subject))

# 어떤글자를 포함하는( 제목, 본문)  메일 가져오기 
# : 항상 작은따옴표 '' 로 먼저 감싸고. 실제 TEXT 부분은 큰따옴표 "" 로 감싼다
# for msg in mailbox.fetch('(TEXT "test mail")',limit=3, reverse=True):
#     print("[{}] {}".format(msg.from_, msg.subject))

# for msg in mailbox.fetch('(SUBJECT "test")'):# 어떤 글자를 포함한는 메일(제목만)
#     print("[{}] {}".format(msg.from_, msg.subject))

# 어떤글자(한글)를 포함하는 메일 필터링(제목만)
#   for msg in mailbox.fetch(limit=5, reverse=True):
#       if "테스트" in msg.subject:
#           print("[{}] {}".format(msg.from_, msg.subject))


# 메일검색2   08:32:31
# # 특정날짜 이후의 메일 가져오기 : SENTSINCE
#       for msg in mailbox.fetch('(SENTSINCE 09-JAN-2022)', limit=5, reverse=True):
#           print("[{}] {}".format(msg.from_, msg.subject))

# # 특정날짜에 온 메일 가져오기 : ON
#       for msg in mailbox.fetch('(ON 09-JAN-2022)', limit=5, reverse=True):
#           print("[{}] {}".format(msg.from_, msg.subject))


#  import time
#  print(time.strftime('%a-%d-%b-%Y')) # 현재 날짜를 요일-일-월-년도 , f= 포멧

#  import datetime
#  dt = datetime.datetime.strptime("2022-01-09", "%Y-%m-%d") # p:파싱
#  print(type(dt))
#  print(dt.strftime('%d-%m-%Y'))

#  #quarry 는 구글에서 imap tools 를 검색하면 # 08:36:36~~
#  # 쿼리에 대한 자세한 사용법을 알수 있음

#  2가지 이상의 조건을 모두 만족하는 메일( AND 조건)
# ON 09-JAN-2022 하나 , SUBJECT "test" 둘
# '(ON 09-JAN-2022 SUBJECT "test")' 계속조건을 주려면 한칸 띄우고 계속 조건을 작성하면 됨

    # for msg in mailbox.fetch('(ON 09-JAN-2022 SUBJECT "test")', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))


#  2가지 이상의 조건중 하나라도 만족하는 메일( OR 조건)  
# ON 09-JAN-2022 하나 , SUBJECT "test" 둘  앞쪽에 OR를 써 준다
# '(ON 09-JAN-2022 SUBJECT "test")' 계속조건을 주려면 한칸 띄우고 계속 조건을 작성하면 됨

    for msg in mailbox.fetch('(OR ON 09-JAN-2022 SUBJECT "test")', limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))


