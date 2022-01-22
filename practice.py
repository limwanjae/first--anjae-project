'''숫자형'''
'''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3*2))

'''

'''문자열'''
'''
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*8)

'''

# 참 / 거짓
'''
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not (5 > 10))

'''

#변수 
#애완동울을 소개해 주세요~
'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal+"의 이름은 "+ name +"예요")
print( name +"는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print( name +"는 어른일까요?" + str(is_adult))

'''
'''
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 "+ animal+"의 이름은 "+ name +"예요")
print( name +"는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print( name +"는 어른일까요?" + str(is_adult))
'''

#여러줄 주석처리 : 콘트롤 + /

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 "+ animal+"의 이름은 "+ name +"예요")
# print( name +"는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
# print( name ,"는 ",age,"살이며, ", hobby,"을 아주 좋아해요")
# print( name +"는 어른일까요?" + str(is_adult))

# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : StopIteration
# 변수값
# : "사당", "신도림", "인천공항" 순서대로 입력

# 출력문장
# : xx행 열차가 들어오고 있습니다.StopIteration

# station = "사당"
# print(station+"행 열차가 들어오고 있습니다.")


## 연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3)# ~승
# print(5%3) #나머지
# print(10%3)

# print(5//3) # 몫
# print(5//3)

# print(10 > 3)
# print(3 <=1 )

# print( 3 == 3) # True
# print(4 == 2) #False
# print(3+4 == 7) #True

# print(1 != 3) #True
# print(not (1 != 3) )# False

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) # True
# print(5 > 4 > 7) #False

# 간단한 수식

# print(2 + 3 * 4) #14
# print((2 + 3) * 4) #20

# number = 2 + 3  *4 #14
# print(number)

# number = number + 2 #16
# print(number)

# number += 2 #18
# print(number)

# number *= 2 #36
# print(number)

# number /= 2 #18
# print(number)

# number -= 2 #16
# print(number)

# number %= 5 #1 나머지
# print(number)

# 숫자처리 함수

# print(abs(-5)) #5 절대값
# print(pow(4,2)) #16  4의 2승,  4^2 = 4*4
# print(max(5,12))#12 최대값
# print(min(5,12))#5 최소값
# print(round(3.14)) # 3 반올림
# print(round(4.99)) # 5 반올림

#rint(sqrt(16)) #4 제곱근


# # 랜덤함수

# from _typeshed import Self
# from random import *
# from typing import NamedTuple

# print(random()) # 0.0~1.0미만의 임의의  값을 생성
# print(random()*10) # 0.0~10미만의 임의의  값을 생성
# print(int(random()*10)) # 0.0~10미만의 임의의  값을 생성
# print(int(random()*10)) # 0.0~10미만의 임의의  값을 생성
# print(int(random()*10)) # 0.0~10미만의 임의의  값을 생성
#print((int(random()*35))+1) # 0.0~36이하의 임의의  값을 생성

# print((int(random()*44))+1) # 1~45이하의 임의의  값을 생성
# print((int(random()*44))+1) 
# print((int(random()*44))+1) 
# print((int(random()*44))+1) 
# print((int(random()*44))+1) 
# print((int(random()*44))+1)  

# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randrange(1,46)) 
# print(randrange(1,46)) 
# print(randrange(1,46)) 
# print(randrange(1,46)) 
# print(randrange(1,46)) 

# print(randint(1,45)) # 1~45 사이의 임의의 값 생성
# print(randint(1,45)) 
# print(randint(1,45)) 
# print(randint(1,45)) 
# print(randint(1,45)) 
# print(randint(1,45)) 

# quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 원별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비해야 하므로 제외

# (출력문 예제)

# 오프라인 스터디 모임날짜 매월 x일로 선정되었습니다.

# from random import *

# date = randint(4, 28)

# print("오프라인 스터디 모임날짜 매월 " + str(date) + " 일로 선정되었습니다.")


## 문자열

# sentence = '나는 소년 입니다'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """

# 나는 소년이고,
# 파이썬은 쉬워요

# """

##슬라이싱

# jumin = "990120-1234567"

# print("성별 : " +jumin[7])
# print("년:"+jumin[0:2]) # 0부터~ 2 직전까지
# print("월 : " + jumin[2:4]) # 2부터~ 4직전까지
# print("일 : " + jumin[4:6]) # 4부터~ 6 직전까지
# print("생녕월일 : " +jumin[0:6])
# print("생년월일 : " +jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 :" + jumin[7:14])
# print("뒤 7자리 :" + jumin[7:]) # 7번째부터 끝까지
# print("뒤 7자리 (뒤에서부터):" + jumin[-7:]) 

##문자열 처리함수

#python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper()) # 대문자인지 확인
# print(len(python)) # 길이
# print(python.replace("Python","java")) # 글자 바꾸기

#index = python.index("n")
# print(index)
# index = python.index("n",index + 1)
# print(index)

# print(python.find("java")) # finds는 글자가 없으면 -1 출력
# #print(python.index("java")) # index에서는 글자가 없으면 에러처리

# print(python.count("n")) # n이 몇번 나오는지 : 2

##문자열 포맷

# print("a" + "b")
# print("a" , "b")

# 방법 1
# print("나는 %d살 입니다." % 20) # 정수
# print("나는 %s을 좋아합니다." %"파이썬") # 문자열
# print("Apple은 %c로 시작해요" % "A") # 문자
# # %s :  문자건, 숫자건 관계없이 잘 됨
# print("나는 %s살 입니다." % 20)
#print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))


#방법2

# print("나는 {}살입니다.". format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 중괄호 연속적으로 입력
# print("나는 {0}색과 {1}색을 좋아해요." .format("파랑", "빨강")) # 중관호에 숫자넣으면 순서대로 
# print("나는 {1}색과 {0}색을 좋아해요." .format("파랑", "빨강"))

#방법 3

# print("나는 {age}살이며, {color}색은 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색은 좋아해요." .format(color = "빨간",age = 20))

# 방법4 (v.3.6이상 부터 됨)

# age = 20
# color = "빨간"

#print(f"나는 {age}살이며, {color}색은 좋아해요.")


## 탈출문자
# \n : 줄바꿈
#print("백문이 불여일견 \n백견이 불여일타")

# \"  \' : 문장내에서  따옴표로 사용
# 저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장네에서는  \로 됨
#print("C:\\Users\\lim")

# \r : 커서를 맨앞으로 이동
#print( "Red Apple\rPine")

# \b : 백스페이스( 한글자 지우기)
#print("Redd\bApple")
#print("Redd\b")

# \t : 탭
#print('red\tApple')                                   

# 퀴즈) 
# 예 ) http://naver.com
# 규칙1 : http://부분은 제외 ==> naver.com
# 규칙2 : 처음 만나는 점 이후 부분은 제외 ==> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 +글자내 'e'갯수 +"!"로 구성
#         ( nav)                     5              1        !
# 예) 생성된 비밀번호 : nav51!

## 풀이)
#url =  "http://naver.com"
#url = "http://daum.net"
#url = "google.com"
# url = "youtube.com"
# my_str = url.replace("http://", "") #규칙1

# my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] -->0~5직전까지.(0,1,2,3,4)
# #print(my_str)
# password = my_str[:3] +str(len(my_str)) + str(my_str.count('e')) + "!"
# print("{0}의 비밀번호는 {1} 입니다 " .format(url, password))


## 리스트 : 순서를 갖는 객체의 집합 []

# 지하철 칸별로 10명,20명,30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
#print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석씨와 조세호씨 사이에 태움
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # subway.pop()
# # print(subway)

# # subway.pop()
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]

# num_list.sort() # 순서대로 정렬
# print(num_list)

# num_list.reverse() # 순서 뒤집기
# print(num_list)
 
# num_list.clear() # 모두 지우기
# print(num_list)

# mix_list = ["조세호",20, True]# 다양한 자료형 함께 사용해도 됨
# print(mix_list)

# num_list = [5,2,4,3,1]
# mix_list = ["조세호",20, True]
# num_list.extend(mix_list) # 리스트 확장
# print(num_list)


## 사전 {}

# cabinet = {3:"유재석", 100:"김태호"} # 사전 - 정수형
# # print(cabinet[3])
# # print(cabinet[100])

# # print(cabinet.get(3))
# # print(cabinet.get(5)) #  키에 5가 없을때는 none 출력하고 다음 프로세스 진행
# # print(cabinet.get(5,"사용가능")) #  키에 5가 없을때는 none 말고 "값" 출력하고싶을 때
# # print("Hi~")
# # print(cabinet[5]) # 키에 5가 없어서 에러 발생시키고 종료
# # print("Hi~")

# # print(3 in cabinet) # True   in을 사용해서 사전에 자료가 있는지 확인
# # print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"} # 사전 - 실수형
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님 # del 이용

# del cabinet["A-3"]
# print(cabinet)

# # key들 만 출력
# print(cabinet.keys())

# # value들 만 출력
# print(cabinet.values())

# # key,value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

## 튜플

# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])

# #menu.add("생선까스")

# # name = "김종국"
# # age = 20
# # hobbby = "코딩"
# # print(name,age,hobbby)

# (name,age,hobby) = ("김종국",20,"코딩")
# print(name,age,hobby)


# ## 집합 (set)
# # 중복이 안되고 ,순서가 없음

# my_set = {1,2,3,3,3}
# print(my_set) # 1,2,3

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합(java와 python 을 모두 할 수 있는 사람)
# print(java & python)
# print(java.intersection(python))

# # 합집합
# print(java | python) 
# print(java.union(python))

# # 차집합(java는 할줄 알지만  python은 할 줄 모르는 사람 )
# print(java-python)
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 까 먹었어요
# java.remove("김태호")
# print(java)

# ## 자료구조의 변경
# #커피숖
# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu) #['커피', '우유', '주스']
# print(menu, type(menu))

# menu = tuple(menu) #('커피', '우유', '주스')
# print(menu, type(menu))

# menu = set(menu) #{'커피', '우유', '주스'}
# print(menu, type(menu))  

#퀴즈 4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨,3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4,5]
# -- 축하합니다 --
# (활용예제)

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # lst 안의 값을 무작위로 바꿈
# print(lst)
# print(sample(lst, 1)) # 랜덤으로 1개 값 추출
# from random import *
# users = range(1,21) #1부터 20까지 숫자를 생성
# #print(type(users))
# users = list(users)
# #print(type(users))
# print(users)
# shuffle(users)
# print(users)
# winners = sample(users,4) #4명 중에서 1명은 치킨,3명은 커피

# print("-- 당첨자 발표 --")
# print(" 치킨 당첨자 : {0}".format(winners[0]))
# print(" 커피 당첨자 :{0}".format(winners[1:]))
# print("-- 축하합니다 --") 

## if문   1:57:33

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈": #조건비교 맞으면 아래 실행, 아니면 elif 비교
#     print("우산을 챙기세요") # 실행문 입력
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:                          # 위 조건이 맞지않으면 출력
#     print("준비물 필요 없어요")

# ##기온 : 항상 숫자
# temp = int(input("기온이 어때요?"))
# if 30<= temp:
#      print("너무 더워요, 나가지 마세요")
# elif 10<= temp and temp < 30 :
#     print("괜찮은 날씨예요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")

## for 문 : 반복문 2:05:09

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 {0}".format(waiting_no))


# for waiting_no in range(5): # 5미만까지
#     print("대기번호 {0}".format(waiting_no))

# for waiting_no in range(1,6): # 1에서 6 미만까지
#     print("대기번호 {0}".format(waiting_no))


# starbucks = ["아이언맨","토르","아이엠 구루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

## while 문 : ~조건 을 만족할때 까지

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0},커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")


# customer = "아이언맨"  # 무한루프  :  콘트롤 +C 로 종료
# index = 1
# while True:
#     print("{0},커피가 준비 되었습니다. 호출{1}회".format(customer,index))
#     index += 1


# customer = "토르"
# person = "unknown"

# while person != customer :
#     print("{0},커피가 준비 되었습니다." .format(customer))
#     person = input("이름이 어떻게 되세요? ")


# absent = [2,5] # 결석
# no_book = [7] #책을 깜박했음
# for student in range(1,11): # 1~10번까지
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{}는 교무실로 따라와".format(no_book))
#         break
#     print("{}, 책을 읽어봐".format(student))

## 한줄 for

# 출석번호가 1,2,3,4,...인대
# 규칙이 바뀌어서 100을 붙이기로 함 --> 101,102,103,104...

# students = [1,2,3,4,5]
# print(students)

# students = [i+100 for i in students]
# print(students)

## 학생이름을 길이로 변환

# students = ["Iron man","Thor","I am groot"]
# students = [len(i) for i in students]
# print(students)

## 학생이름을  대문자로
# students = ["Iron man","Thor","I am groot"]
# students = [i.upper() for i in students]
# print(students)

##퀴즈) 당신은 Cocoa서비스를 이용하는 택시 기사입니다.
# 50명의 승객가 매칭기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0]1번째 손님 (소요시간 : 15분)
# []2번째 손님 (소요시간 : 50분)
# [0]3번째 손님 (소요시간 : 5분)
# ...
# [0]50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

# from random import *
# cnt = 0 #총 탑승 승객 수

# for i in range(1,51): # 1~50 승객
#     time = randrange(5,51) # 5~50분 소요시간
#     if 5 <= time <= 15: # 5분~15분 이내의 손님(매칭 성공), 탑승 승객 수 증가처리
#         print("[0]{0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[0]{0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0}분".format(cnt))

## 함수

# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")

# open_account()

# ## 전달값 , 반환값

# ## 입금하는 함수
# def deposit(balance, money): # 입금
#     print("입금이 완료 되었습니다.잔액은{0}원입니다.".format(balance + money))
#     return balance + money

# ## 출금하는 함수

# def withdraw(balance,money): # 출금
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance - money
#     else : 
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
#         return(balance)

# def withdraw_night(blance, money): #저녁에 출금, 수수료
#     commission = 100 #수수료 100원
#     return commission, balance - money - commission


# balance = 0 # 잔액
# balance = deposit(balance,1000)
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance,500)
# print("수수료는 {0}원이며, 잔액은 {1}원 입니다".format(commission,balance))

## 함수에서 기본값 설정하는 방법   , \ : 줄바꿈 했지만 한문장

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# ## 같은 학교,같은 학년, 같은반, 같은 수업을 듣는다면 
# ## 매번 프로필에 공통되는것을 지정해 줌 

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

## 키워드 값을 이용한 함수 호출

# def profile (name, age, main_lang):
#     print(name,age,main_lang)
    
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25,name="김태호")

## 가변 인자(*)를 통한 함수 호출

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ") # end=" " 는 이어서 계속 출력한다는 것
#     print(lang1, lang2, lang3, lang4, lang5)


# def profile(name,age,*language): # 가변인자 *
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ") # end=" " 는 이어서 계속 출력한다는 것
#     for lang in language:
#         print(lang,end=" ")
#     print()

# profile("유재석",20, "python", "java", "c", "c++", "c#","javascript") # 2:45:03
# profile("김태호", 25,"kotlin", "swift", "", "","")

# #지역변수 ,전역변수
# gun =10

# # def checkpoint(soldiers): #경계근무
# #     #gun =20  # 지역변수
# #     global gun # global을 붙여서 전역공간에 있는 gun 사용하겠다는 뜻
# #     gun = gun - soldiers
# #     print("[함수 내] 남은 총 : {0}".format(gun))

# # print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계근무를 나감
# # print("남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


# #퀴즈) 표준 체중을 구하는 프로그램을 작성하시오

# *표준체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x키(m) x 22
# 여자 : 키(m) x키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# # (출력 예제)
# # 키 174cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender): #키는 m단위(실수),성별은 "남자"/"여자"
#     if gender == "남자":
#       return height * height * 22
#     else:
#         return height * height * 21

# height = 175# cm
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

## 표준 입출력

# print("python", "java") # python java
# print("python" +"java") # pythonjava
# print("python", "java",sep=",") # python,java
# print("python", "java","javascript", sep=" vs ") # python vs java vs javascript
# print("python", "java",sep=",", end="?") # 문장의 끝부분을 ?로 해달라
# print("무엇이 더 재미있을까요?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject,score)
    
# # 수학 0
# # 영어 50
# # 코딩 100

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
  
#     print(subject.ljust(8),str(score).rjust(4),sep=":") # .ljust(8):왼쪽에서 8칸에 줄 맞추기
#                                            # .rjust(4):오른쪽에서 4칸 줄 맞추기

# # 수학      :   0
# # 영어      :  50
# # 코딩      : 100

# # 대기 순번표 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " +str(num).zfill(3)) # z.fill : 3개 공간 확보, 빈공간은 영을 채우는 것


## 표준입력

# answer = input("아무거나 입력하세요 : ") # 사용자 입력으로 숫자를 받아도 항상 문자열로 인식한다
# print(type(answer))
# print("입력하신 값은 " + answer +"입니다")

# ## 다양한 출력 포맷 3:10:57

# # 빈 자리는 빈 공간으로 두고, 오른쪽 정력을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일때는 +로 표시,음수일때는 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽으로 정렬하고,빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# # 3자리 마다 콤마를 찍어주고, + -부호도 붙이기
# print("{0:+,}".format(100000000))
# # 3자리 마다 콤마를 찍어주고, + -부호도 붙이기, 30자리수 확보하기
# #돈이 많으면 행복하니까 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 2자리수 까지만 출력( 소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# # 파일에 내용 입력
# score_file = open("score.txt","w",encoding="utf8") # w는 쓰기
# print("수학 : 0",file = score_file)
# print("수학 : 50",file = score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8") #a는 append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # \n 는 줄바꿈
# score_file.close()

# # 파일속의 내용 읽어오기

# score_file = open("score.txt","r" ,encoding="utf8") # r는 읽기
# print(score_file.read()) # 한번에 모든내용 읽어오기
# score_file.close()


# score_file = open("score.txt","r" ,encoding="utf8") # r는 읽기
# print(score_file.readline()) # 줄별로 읽고, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # print에서는 자동으로 줄 바꿈에 됨
# print(score_file.readline())
# print(score_file.readline())

# score_file = open("score.txt","r" ,encoding="utf8") # r는 읽기
# print(score_file.readline()) # 줄별로 읽고, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # print에서는 자동으로 줄 바꿈에 됨
# print(score_file.readline(), end="") # 줄바꿈을 안 하려면
# print(score_file.readline(), end="")

# # 읽어올 파일이 몇 줄인지 모를때 줄 별로 읽기

# score_file = open("score.txt","r" ,encoding="utf8") # r는 읽기
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")  # end=""는 줄바꿈 안 함
# score_file.close()

# # 리스트에 넣어서 처리할 수 있음

# score_file = open("score.txt","r", encoding="utf8")
# lines = score_file.readlines() # 리스트 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle : 프로그램에서 쓰는 데이터를 파일형태로 저장한 것을
# 다른 사람에게 주었을때 pickle로 읽어서 또 사용할 수 있는것 

# # 저장하기
# import pickle
# profile_file = open("profile.pickle","wb") #  "wb" 피클은 바이너리 형태로 쓰기 해야함
# profile = {"이름":"박명수","나이" : 30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 file에 저장
# profile_file.close()

# # 저장된 파일에서 읽어오기
# import pickle
# profile_file = open("profile.pickle","rb")  #  "rb" 피클은 바이너리 형태로 읽기 해야함
# profile = pickle.load(profile_file) #file에 있는 정보를 프로필에 불러오기
# print(profile)
# profile_file.close()


#  # with :파일을 열고, 저장하기를 좀 편하게 할 수 있음

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# # with를 활용해서 파일에 쓰고, 읽기 ,with는 매번 파일을 클로즈 안 해도 돼서 편리함
# # with를 활용해서 파일에 쓰고
# # with open("study.txt", "w", encoding="utf8") as study_file:
# #     study_file.write("파이썬을 열심히 공부하고 있어요")

# # with를 활용해서 파일에 읽기
# with open("study.txt", "r", encoding="utf8") as study_file:
#      print(study_file.read())

# # 퀴즈) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# # 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# # - x 주차 주간보고 -
# # 부서 :
# # 이름:
# # 업무요약:

# # 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# # 조건 : 파일명은 1주차.txt, 2주차.txt, ... 와 같이 만듭니다.

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file: # w모드라서 덮어쓰기 할 것임.
#         report_file.write("- {0}주차 주간보고 -".format(i))
#         report_file.write("\n부서 :") #  \n 줄바꿈
#         report_file.write("\n이름:")
#         report_file.write("\n업무요약:")


# # 클래스 3:38:43

# # 마린 : 공격유닛,군인, 총을 쏠수 있음
# name = "마린" #  유닛의 이름
# hp = 40      # 유닛의 체력
# damage = 5   # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격유닛, 탱크, 포를 쏠수있는데, 일반모드/시즈모드 

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 공격함수
# def attack(name, location, damage):
#     print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))


# # 탱크를 하나더 추가 한다면
# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 매번  탱크를 추가하기 힘드니까 클래스를 사용한다
# # 클래스는 붕어빵 틀 같은 것 : 변수와 함수의 집합      3:44:34

# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 마린 유닛이 생성 되었습니다.
# 체력 40, 공격력 5
# 탱크 유닛이 생성 되었습니다.
# 체력 150, 공격력 35

# __init__ 함수  3:47:12
# 멤버변수
# # 레이스 : 공중 유닛, 비행기, 클로킹( 상대방에게 보이지 않음)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 콘트롤 : 상대방의 유닛을 내 것으로 만드는것(빼앗음)

# wraith2 = Unit("빼앗은레이스", 80, 5)
# wraith2.clocking = True #클래스 외부에서 변수 확장이 가능

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# ## 메소드 
# # 일반 유닛
# class Unit : 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage


# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은{1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# # 메딕 : 의무병

# # 파이어 뱃 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# ## 상속 3:59:32, Unit 와 AttackUnit에서 겹치는것( name 과 hp)을 상속시킴

# # 일반 유닛
# class Unit : 
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
 
# class AttackUnit(Unit): # 어택유닛이 일반유닛을 상속받음
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name, hp)       
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은{1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# # 드랍쉽 :공중 유닛, 수송기,마린/파이어뱃/탱크 등을 수송,공격은 불가

# #날 수 있는 기능을 가진 클래스
# class Flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): #어택유닛 과 Flyable 상속 받음
#     def __init__(self, name, hp, damage, flying_speed): # 초기화
#         AttackUnit.__init__(self, name, hp, damage) # 초기화
#         Flyable.__init__(self, flying_speed) # 초기화
        
# # 발키리 : 공중공격 유닛,한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5 )
# valkyrie.fly(valkyrie.name, "3시")


# ## 오버라이딩 : "부모 메소드"에서 쓴 걸 "자식 메소드"에서 쓸수 있게 하는것

# # 일반 유닛
# class Unit : 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(Unit): # 어택유닛이 일반유닛을 상속받음
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)       
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은{1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# #날 수 있는 기능을 가진 클래스
# class Flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): #어택유닛 과 Flyable 상속 받음
#     def __init__(self, name, hp, damage, flying_speed): # 초기화
#         AttackUnit.__init__(self, name, hp, 0, damage) # 초기화, 지상 speed는 0
#         Flyable.__init__(self, flying_speed) # 초기화

#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, location)

# #벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀크루저 : 공중 유닛, 체력도 굉장히 좋음,공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시")


# ## pass 4:17:07

# class Unit : 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# # 서플라이 디폿 : 건무ㄹ, 1개 건물= 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()


# ##super

# class Unit : 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location


# ## 스타그래프트 전반전

# from random import *

# # 일반 유닛
# class Unit : 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은{1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))

# # 공격 유닛
# class AttackUnit(Unit): # 어택유닛이 일반유닛을 상속받음
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)       
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은{1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴 되었습니다.".format(self.name))
        
# #날 수 있는 기능을 가진 클래스
# class Flyable: 
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): #어택유닛 과 Flyable 상속 받음
#     def __init__(self, name, hp, damage, flying_speed): # 초기화
#         AttackUnit.__init__(self, name, hp, 0, damage) # 초기화, 지상 speed는 0
#         Flyable.__init__(self, flying_speed) # 초기화

#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, location)

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정시간 동안 이동 및 공격속도를 증가,체력10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0}: 스팀팩을 사용합니다. (hp 10 감소".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다.".format(self.name))

# #탱크 4:28 :09
# class Tank(AttackUnit):
#     #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격가능.이동은 불가
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때: 시즈모드를 하면 되고
#         if  self.set_seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True

#         # 현재 시즈모드 일 때 : 시즈모드 해제 하면 됨
#         else:
#             print("{0} : 시즈모드로 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False  

# # 레이스
# class wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드(해제상태)

#     def clocking(self):
#          # 현재 클로킹 모드가 일 때: 클로킹 모드를 해제하면 되고
#         if  self.clocked == True:
#             print("{0} : 클로킹모드 해제합니다.".format(self.name))
#             self.clocked = False

#         # 현재 클로킹 모드가 아닐 때 : 클로킹 모드로 하면 됨
#         else:
#             print("{0} : 클로킹모드로 설정합니다.".format(self.name))
#             self.clocked = True 

# ## 스타그래프트 후반전 4:34:07
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("player : gg") # good game
#     print("[player]님이 게임에서 퇴장하셨습니다.")

# #  게임 시작

# # 마린 3기 생성
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = wraith()

# # 유닛 일괄 관리(생선된 모든 유닛 append)

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(m1)
# attack_units.append(t1)
# attack_units.append(t1)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발 04:37:07
# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료 되었습니다.")

# # 공격 모드 준비( 마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹 )
# for unit in attack_units:
#     if isinstance(unit, Marine): # 지금 만들어진 인스턴스 확인해서 맞는처리를 한는것
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해 4:39:57
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음( 5~20 )

# # 게임 종료
# game_over()



# ##퀴즈) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오. 4:44:50

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price,\
#          completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year


#     #매물정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type,\
#              self.price, self.completion_year)
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억","2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

## 예외처리1 : 에러가 났을때 처리해 주는 것 : 4:50
# try:
#     print("나누기 전용 계산기입니다.")
    
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

# 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 6
# 두 번째 숫자를 입력하세요 : 0
# division by zero

## 예외처리2
# try:
#     print("나누기 전용 계산기입니다.")
#     nums =[]
#     nums.append( int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)

# # 나누기 전용 계산기입니다.
# # 첫 번째 숫자를 입력하세요 : 6
# # 두 번째 숫자를 입력하세요 : 3
# # 알 수 없는 에러가 발생했습니다.
# # list index out of range

##  에러 발생 시키기 4:58:17


# ## 모듈 : 같은 폴더내에 있으면 그냥 불러서 쓸수 있음
# import theater_module
# theater_module.price(3) # 3명이 영하 보러 갔을때 가격
# theater_module.price_morning(4) # 4명이 조조 할인 영하 보러 갔을때
# theater_module.price_soldier(5) # 5명 군인이 영화 보러 갔을 때

# # 3명 가격은 30000원 입니다.
# # 4명 조조 할인 가격은 24000원 입니다.
# # 5명 군인 할인 가격은 20000원 입니다.

# import theater_module as mv # 모듈명이 theater_module처럼 길때  별명(mv)으로 호출할 수 있음
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# # 3명 가격은 30000원 입니다.
# # 4명 조조 할인 가격은 24000원 입니다.
# # 5명 군인 할인 가격은 20000원 입니다.

# ## from 모듈명 import *  :  from random import * 하고 같은것 임

# from theater_module import * # 모듈에 있는 모든것을 사용하겠다

# price(3)
# price_morning(4)
# price_soldier(5)

# # 3명 가격은 30000원 입니다.
# # 4명 조조 할인 가격은 24000원 입니다.
# # 5명 군인 할인 가격은 20000원 입니다.

# ## from  import 를 조금 더 변형해서 써 보면( 필요한 것 만 불러다 씀)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)

# # 5명 가격은 50000원 입니다.
# # 6명 조조 할인 가격은 36000원 입니다.

# ## from  import 를 조금 더 변형해서 써 보면( 필요한 것(price_soldier) 만 불러다  별명(price)을 사용 )

# from theater_module import price_soldier as price
# price(5)

# # 5명 군인 할인 가격은 20000원 입니다.


## 패키지 : 모듈들을 모아 놓은 집합 5:25:10
# travel 폴더를 만들고
# 폴더 안에 태국파일, 베트남 파일, __init__ 파일을 만든 다음
# 태국 파일 에는 태국 여행 상품을 정의하고
# 베크남파일에는  베트남 여행 상품을 정의한다
# __init__ 파일은 그대로 둔다.    5:27:28

# import travel.thailand #travel폴더에 thailand 파일을 호출, 파일자리에 클래스나 모듈은 직접쓰면 안됨
# trip_to = travel.thailand.ThailandPackage()  #호출한 travel폴더에 thailand 파일에서 패키지 클래스를 trip_to로 정의
# trip_to.detail() #detail 함수 실행

# # #[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원


# ## from  import를 쓰면  #travel폴더에 thailand 파일을 호출: 파일자리에 클래스나 모듈은 직접쓸수 있음
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage() 
# trip_to.detail()

# #[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원 

# ## 베트남은 다르게 호출해 보면 

# from travel import vietnam
# trip_to = vietnam.VietnamPakage() 
# trip_to.detail()

# # 출력) [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

# ## __all__ 사용 : __init__.py파일에서 __all__ =["파일명"]으로 파일안에 패키지 호출  5:30:40
# # from random import *  # random 모듈안에 있는 모든것(*)을 사용 하겠다
# from  travel import *
# # from travel import thailand
# trip_to = vietnam.VietnamPakage() 
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # [베트남 패키지 3박 5일] 다낭 효도 여행 60만원
# # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# ## 모듈 직접 실행  5:34:16
# # 파일내의 모듈을 쓰는건지 외부파일에서 모듈을 가져다 쓰는건지 확인
# #  
# # 타일랜드 파일에 가서

# # if __name__ == "__main__":
# #     print("Thailand 모듈을 직접 실행")
# #     print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
# #     trip_to = ThailandPackage()
# #     trip_to.detail() 
# # 를 입력하고 실행하면

# #답) Thailand 모듈을 직접 실행
# # 이 문장은 모듈을 직접 실행할 때만 실행돼요
# # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# # practice 파일에서 실행하면

# from  travel import *
# # from travel import thailand
# #trip_to = vietnam.VietnamPakage() 

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # 답)
# # Thailand 외부에서 모듈 호출 <---이렇게 표시
# # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원 

# ## 패키지, 모듈 위치 : 5:37:00

# from  travel import *

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random)) # ramdom이라는 모듈이 어디에 있는지 파일정보를 알려줌.
# print(inspect.getfile(thailand)) 

# 답)
# Thailand 외부에서 모듈 호출
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원 
# C:\Users\lim\AppData\Local\Programs\Python\Python39\lib\random.py
# C:\Users\lim\AppData\Local\Programs\Python\Python39\lib\travel\thailand.py

## pip install : pip로 패키지 설치하는 방법  5:40:30
# 다름사람들이 만들어 놓은 패키기 찾아보기
# 구글 검색창에서 pypi 입력후 검색


#from bs4 import BeautifulSoup
#soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
#print(soup.prettify())



## 내장 함수 :import 필요없이 바로쓸수 있는 함수  5:46:10

# #input : 사용자 입력을 받는 함수

# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다.".format(language))

# # 무슨 언어를 좋아하세요?파이썬
# # 파이썬은 아주 좋은 언어 입니다.

# # # dir : 어떤 객체를 넘겨 줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# # print(dir())
# import random # 외장함수
# # print(dir())
# # import pickle
# # print(dir())

# print(dir(random))

# ## lst
# lst = [1, 2, 3]
# print(dir(lst))

# 답) lst에 대해 쓸수 있는 내장 함수가 나온다
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

##예
# name = "jim"
# print(dir(name))

# 답 : name에 대해 쓸수 있는 내장함수가 나온다

###이것 말고도 구글에서 list of python builtins 검색하면 설명나옴


## 외장함수 5:50:40
# 구글에서 list of pyton modules 검색

# # glob : 경로내의 폴더/파일 목록 조회( 윈도우 dir 과 같은것)
# import glob
# print(glob.glob("*.py")) # py 확장자 파일을 찾아라~~

# 답)
# ['helloworld.py', 'practice.py', 'practice_class.py', 'theater_module.py']

# os : 운용체계에서 제공하는 기본 기능

#import os
# print(os.getcwd()) # 현재 디렉토리를 표시해라

# 답)
# C:\Users\lim\Desktop\PythonWorkspace

# ## 폴더를 만들고 삭제하는~~
# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# # os.listdir() :  glob 과 비슷한 기능
# import os
# print(os.listdir())

# 답)
# ['helloworld.py', 'practice.py', 'practice_class.py', 'profile.pickle', 'score.txt', 'study.txt', 'theater_module.py', 'travel', '__pycache__']

## time : 시간 관련 함수
#import time
#print(time.localtime())
#print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2021-10-14 00:27:07

# import datetime
# #print("오늘 날짜는 ", datetime.date.today()) #오늘 날짜는  2021-10-14

# # timedelta : 두 날짜 사이 간격
# import datetime
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days = 100) # 100일 저장
# print("우리가 만난지 100일은 ", today +td) # 오늘부터 100일 후 정보를 알려줌
#답)우리가 만난지 100일은  2022-01-22


#퀴즈10) 5:58:47
#프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

#조건 : 모듈 파일명은 byme.py 로 작성

#(모듈 사용 예제)

import byme
byme.sign()

#(출력예제)
#이 프로그램은 나도코딩에 의해 만들어졌습니다.
#유튜브 : http://youtube.com
#이메일 ; nadocoding@gmail.com







