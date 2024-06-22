from bs4 import BeautifulSoup
import requests
import smtplib
import json
import time

address_path = 'secret.json'
smtp = "smtp.gmail.com"
port = 587

target_time = "21:20"
target_price = 130
product_url = "https://www.amazon.com/Seagate-Expansion-Desktop-Drive-Black/dp/B07VS8QCXC/ref=sr_1_1?crid=1YXA3ADINFS8O&dib=eyJ2IjoiMSJ9.O-iz_OxFgbx8bLQuv31KFNq9EqEsv06BvQkuwEn6cNPNtFGUdYqwHmnbzkunELII3GzVPoGIDiQUnkTCGdDqjQly1Fhy8RbRdvxYRjrrcAG4n8hLu605tUVwzGp_Ft1N9Nz7RQqs26WYAQsuENh_GXyxzssO78dshrh_jodARrBN_Dp8LGOVPPKvhLVyFw7tui9ggRl03cAFSKPv2iVV-MXw-Z3-lIMBG3QXB21Khso.I3JpZThvqbKGyQYrEMFHxSSXuMTPDdCwL__aAMPv4Mo&dib_tag=se&keywords=portable%2Bhard%2Bdisk%2B8tb&qid=1719035880&sprefix=portablehard%2Bdisk%2B8tb%2Caps%2C221&sr=8-1&th=1"


send_price = 0
# 메인 함수
if __name__ == "__main__":
    # 가격 찾기
    # External HDD : 5TB
    response = requests.get(url=product_url)
    soup = BeautifulSoup(response.text, 'lxml')
    object_price = soup.select_one(
        "td._product-comparison-desktop_desktopFaceoutStyle_asin-0__3hzbG span span.a-offscreen")
    price = float(object_price.getText().strip('$'))
    print("price get")
    if price <= target_price:
        # load address info
        with open(address_path, 'r') as file:
            data = json.load(file)
            MY_EMAIL = data["MY_EMAIL"]
            TOKEN_PW = data["TOKEN_PW"]
            TO_MAIL = data["TO_MAIL"]
        msg = f"Subject:Amazon HDD sale! ${price} !!\n\n"

        msg += f"HDD 5TB price is {price} !!\n"
        msg += f'판매 링크\n{product_url}'
        # asw 용 encoding
        msg = msg.encode('utf8')
        # mail 보내기
        with smtplib.SMTP(smtp, port=port) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=TOKEN_PW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_MAIL,
                msg=msg
            )
        print("mail send")
    # 1시간 마다 실행
    else:
        time.sleep(60)

# --------- 원하는 옵션 코드 찾기 -------------
# print(soup.prettify())
# price_tags = soup.find_all(class_="a-offscreen")

# 각 태그의 상위 경로와 클래스 정보 출력
# 상품 태그 출력
# for tag in price_tags:
#     path = []
#     parent = tag
#     while parent is not None:
#         tag_name = parent.name
#         tag_classes = parent.get('class', [])
#         if tag_classes:
#             path.append(f"{tag_name}({' '.join(tag_classes)})")
#         else:
#             path.append(tag_name)
#         parent = parent.parent
#     path.reverse()  # 루트부터 경로를 출력하기 위해 순서를 뒤집습니다.
#     print(' > '.join(path), tag.getText())
