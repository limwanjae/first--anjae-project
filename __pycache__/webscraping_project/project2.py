#[IT뉴스]
# 1. 무슨 무슨 일이...
# (링크 : https://...
# 2. 어떤 어떤 일이...
# (링크 : https://...
# 3. 이런 저런 일이...
# (링크 : https://...

import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

def print_news(index, title, link):
    title = news.find("a").get_text().strip()
    link = news.find("a")["href"]


def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)# 3개 까지만 가져오기
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = news.find("a")["href"]
        print_news(index, title, link)
    print()

if __name__ == "__main__":
    scrape_it_news()# it 뉴스정보 가져오기