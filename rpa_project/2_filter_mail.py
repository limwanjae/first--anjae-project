# 메일 필터링
# 받은메일 내용중에서 
# 본문 : 닉네임/전화번호 뒤 4자리(random)
#   (예) 나도코딩/1234
# 를 가져와서 저장
from account import *
from imap_tools import MailBox

applicant_list = []# 지원자 리스트

with  MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:

    index = 1 # 순번을 저장하기 위한 변수
    for msg in mailbox.fetch('(SENTSINCE 10-JAN-2022)'): # 2022년 1월10일 이후로 온 메리 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임: {} 전화번호: {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)
# (<imap_tools.message.MailMessage object at 0x0000019D8F9D4850>, 1, '유재석', '4691')
# (<imap_tools.message.MailMessage object at 0x0000019D8F9D4550>, 2, '박명수', '7436')
# (<imap_tools.message.MailMessage object at 0x0000019D8F9D4D30>, 3, '정형돈', '9588')
# (<imap_tools.message.MailMessage object at 0x0000019D8F9D7A00>, 4, '노홍철', '6423')
# (<imap_tools.message.MailMessage object at 0x0000019D8F9D7B50>, 5, '조세호', '5326')

