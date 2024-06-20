from bs4 import BeautifulSoup
import requests
import ssl
import pandas as pd
import datetime

today = datetime.date.today().strftime("%Y%m%d")

headlines = []
links = []
# 네이버 뉴스 3페이지까지 스크래핑
for i in range(1, 4):
    response = requests.get(f"https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=009&date={today}&page={i}",
                            verify=False)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all(name='a', class_='nclicks(cnt_flashart)')

    for i, article in enumerate(articles):

        headline = article.getText().strip()
        if headline != "":
            headlines.append(headline)
            links.append(article.get('href'))

data = {'헤드라인': headlines,
        'link': links}
article_csv = pd.DataFrame(data)

article_csv.to_csv(f"{today}_매일경제.csv", encoding='utf-8-sig')
