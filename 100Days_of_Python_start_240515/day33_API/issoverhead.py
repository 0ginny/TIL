import requests
from datetime import datetime
import smtplib
import time

ADDRESS_TXT = '../day32_automated_birth_wisher/address.txt'
MY_LAT = 36.642546
MY_LONG = -127.490814
ERROR_RANGE = 5
STMP = 'stmp.google.com'
STMP_PORT = 587

with open(ADDRESS_TXT) as file :
    data = file.readlines()
    MY_ADDRESS = data[0].rstrip('\n')
    MY_PW = data[2].rstrip('\n')
    TO_ADDRESS = data[3].rstrip('\n')

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
min_iss_lat = iss_latitude - ERROR_RANGE
max_iss_lat = iss_latitude + ERROR_RANGE
min_iss_long = iss_longitude - ERROR_RANGE
max_iss_long = iss_longitude + ERROR_RANGE

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

#If the ISS is close to my current position
while 1:
    if min_iss_long <= MY_LONG <= max_iss_long and min_iss_lat <= MY_LAT <= max_iss_lat:
    # and it is currently dark
        if hour > sunset :
            # Then send me an email to tell me to look up.
            with smtplib.SMTP(STMP, STMP_PORT) as connection:
                connection.starttls()
                connection.login(user=MY_ADDRESS, password=MY_PW)
                connection.sendmail(
                    from_addr=MY_ADDRESS,
                    to_addrs=TO_ADDRESS,
                    msg = "Subject:Lock at ISS!\n\nISS is over your head"
                )
    time.sleep(60)

# BONUS: run the code every 60 seconds.



