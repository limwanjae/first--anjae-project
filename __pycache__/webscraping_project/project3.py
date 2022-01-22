import re
import requests
from bs4 import BeautifulSoup


# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : https://...
# 2. 어떤 어떤 일이...
# (링크 : https://...
# 3. 이런 저런 일이...
# (링크 : https://...

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:# 8문장이 있다고 가정할때 ,5~8까지(index기준 4~7) 잘라서 가져옴
        print(sentence.get_text().strip())
    print()

    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:# 8문장이 있다고 가정할때 ,(index기준 0~3) 잘라서 가져옴
        print(sentence.get_text().strip())  

    print()


if __name__ == "__main__":
    scrape_english() # 오늘의 영어회화 가져오기



