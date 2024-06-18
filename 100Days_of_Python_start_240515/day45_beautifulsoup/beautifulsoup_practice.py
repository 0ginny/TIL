from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding='UTF8') as file:
    contents = file.read()

soup = BeautifulSoup(contents,'html.parser')
# print(soup.prettify())
all_anchors = soup.find_all(name='a')
print(all_anchors)

# 내용물만 프린트 하기
for anchor in all_anchors:
    # print(anchor.getText())
    print(anchor.get('href'))

heading = soup.find(name='h1',id='name')
print(heading.getText())

section_heading = soup.find_all(name='h3',class_='heading')
print(section_heading)

test = soup.find(name='p')
print(test)
print(test.getText())

# 아래 구조를 얻을 수 있음. p 아래 a 섹션
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector='#name')
print(name)
