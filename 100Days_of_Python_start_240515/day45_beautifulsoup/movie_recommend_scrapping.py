from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url,verify=False)
soup = BeautifulSoup(response.text,'html.parser')

titles = soup.find_all(name='h3', class_ = "title")

ranks = []
movies = []
print(titles)

for title in titles:
    movies.append(title.getText())
print(movies)
with open('movie_top100.txt','w',encoding='utf-8') as txt:
    for line in movies[::-1]:
        txt.write(f'{line}\n')


