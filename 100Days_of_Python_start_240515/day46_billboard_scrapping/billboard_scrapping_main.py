from bs4 import BeautifulSoup
import datetime
import requests
import pandas as pd

# search_date = input("which year do you want to travel to? (YYYY-MM-DD) ")
search_date = "2022-05-15"

url = f"https://www.billboard.com/charts/hot-100/{search_date}/"

response = requests.get(url,verify=False)
# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')

title_tags = soup.select("li ul li h3#title-of-a-story")
artist_tags = soup.select("li ul li span.a-no-trucate")

pd_data= {
    "title" : [title.getText().strip() for title in title_tags],
    "artist" : [artist.getText().strip() for artist in artist_tags]
}


billboard_pd = pd.DataFrame(data=pd_data)
billboard_pd.index = billboard_pd.index+1
billboard_pd.index.name = 'rank'
# print(billboard_pd)
billboard_pd.to_csv(f"billboard_{search_date}_top100.csv",encoding='utf-8')