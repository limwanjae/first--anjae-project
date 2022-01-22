import requests
from bs4 import BeautifulSoup


# [오늘의 날씨]
# 흐림,어제보다 00높아요
# 현재 ㅇㅇ도씨 ( 최저00 / 최고00)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00 좋음
# 초미세먼지 00좋음

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=5&acq=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8%EC%98%88%EB%B3%B4"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
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
   
if __name__ == "__main__":
    scrape_weather() #오늘의 날씨정보 가져오기
