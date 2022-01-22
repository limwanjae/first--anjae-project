import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=5&acq=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8%EC%98%88%EB%B3%B4"
    soup = create_soup(url)

    # 흐림,어제보다 00높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 ㅇㅇ도씨 ( 최저00 / 최고00)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace("현재온도", "")# 현재온도
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("평균기온", "")#최저온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("평균기온", "")#최고온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    rain_rate = soup.find("div", attrs={"class":"cell_weather"}).get_text().strip()
    
    
    #출력
    print(cast)
    print("{} (최저 {} / {})".format(curr_temp, min_temp, max_temp))
    print(rain_rate)
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip() # = news.div.a.get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()


# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
# (링크 : https://...
# 2. 어떤 어떤 일이...
# (링크 : https://...
# 3. 이런 저런 일이...
# (링크 : https://...

   
if __name__ == "__main__":
    scrape_weather() #오늘의 날씨정보 가져오기
    scrape_headline_news() #
