import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('main.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(["title","who","rate"])

# 우리가 정보를 얻고 싶어하는 URL
WEEK_URL = f"https://comic.naver.com/webtoon/weekdayList?week=wed"
# get 요청을 통해 해당 페이지 정보를 저장
week_html = requests.get(WEEK_URL)
print(week_html)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
week_soup = BeautifulSoup(week_html.text,"html.parser")
# egg_list_box = egg_soup.find("ul",{"class":"list_basis"})
toon_list_box = week_soup.find("div",{"class":"list_area daily_img"})
toon_list = toon_list_box.find_all("li")
result = []
result = extract_info(toon_list)
for info in result:
    row=[]
    row.append(info['title'])
    row.append(info['who'])
    row.append(info['rate'])
    writer.writerow(row)
print(result)