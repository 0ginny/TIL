import smtplib

address_path = 'address.txt'
smtp = "smtp.gmail.com"
port = 587
msg = "Subject:Text\n\nThis is the test message"

with open(address_path) as file :
    text = file.readlines()
    my_address = text[0].rstrip('\n')
    my_pw = text[2].rstrip('\n')
    to_address = text[3].rstrip('\n')

with smtplib.SMTP(smtp,port=port) as connection :
    connection.starttls()
    connection.login(user=my_address,password=my_pw)
    connection.sendmail(
        from_addr=my_address,
        to_addrs=to_address,
        msg = msg
    )