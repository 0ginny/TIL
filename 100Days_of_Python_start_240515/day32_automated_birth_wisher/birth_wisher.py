import smtplib
import datetime as dt
import random as rd

address_path = 'address.txt'
smtp = "smtp.gmail.com"
port = 587
msg = "Subject:Text\n\nThis is the test message"

weekday_for_send_quote = 5

# load address info
with open(address_path) as file :
    text = file.readlines()
    my_address = text[0].rstrip('\n')
    my_pw = text[2].rstrip('\n')
    to_address = text[3].rstrip('\n')

# today weekday
current_weekday = dt.datetime.now().weekday()

with open('quotes.txt','r') as file :
    quotes = [line.rstrip('\n') for line in file.readlines()]


if current_weekday == weekday_for_send_quote :
    msg = f"Subject:Today's quote\n\n{rd.choice(quotes)}"
    with smtplib.SMTP(smtp,port=port) as connection :
        connection.starttls()
        connection.login(user=my_address,password=my_pw)
        connection.sendmail(
            from_addr=my_address,
            to_addrs=to_address,
            msg = msg
        )