import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a 엘리먼트를 출력
#print(soup.a.attrs)# a 엘리먼트의 속성 정보를 출력
#print(soup.a["href"])# a 엘리먼트의 href 속성 '값' 정보를 출력

#print(soup.find("a", attrs={"class":"Nbtn_upload"}))# class "Nbtn_upload"인 "a" 엘리먼트를 찾아줘
#print(soup.find(attrs={"class":"Nbtn_upload"})) #class "Nbtn_upload"인 어떤엘리먼트를 찾아줘

# print(soup.find("li", attrs={"class" : "rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# #print(rank1.a.get_text()) # 랭크1의 문자찾기(출력)

# ########### subling으로 형제 찾기
# #print(rank1.next_sibling)
# # rank2 = rank1.next_sibling.next_sibling
# # rank3 = rank2.next_sibling.next_sibling
# # print(rank3.a.get_text())
# # rank2 = rank3.previous_sibling.previous_sibling
# # print(rank2.a.get_text())
# # print(rank1.parent)
# ############### sibling을 반복하지 않고 찾기~~
# # rank1.find_next_sibling("li")
# # rank2 = rank1.find_next_sibling("li")
# # print(rank2.a.get_text())
# # rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())
# # rank2 = rank3.find_previous_sibling("li")
# # print(rank2.a.get_text())

# ######## 랭크를 한꺼번에 찾기( 출력)
# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="싸움독학-104화 : 나 최보미 좋아한다")
print(webtoon)


