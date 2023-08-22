import requests
from datetime import datetime
import smtplib
import time

MY_LAT = "YOUR LATITUDE"
MY_LONG = "YOUR LONGITUDE"

MY_EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    if -5 <= iss_latitude - MY_LAT <= 5 and -5 <= iss_longitude - MY_LONG <= 5:
        return True
    else:
        return False


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
while True:
    time.sleep(60)
    if is_iss_overhead and (time_now.hour >= sunset or time_now.hour <= sunrise):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="YOUR EMAIL", msg=f"Subject: Look up!\n\n "
                                                                                                  f"The ISS above you and"
                                                                                                  f"its night!\nThe latitude "
                                                                                                  f"of the ISS is: "
                                                                                                  f"{iss_latitude} and its "
                                                                                                  f"longitude is: "
                                                                                                  f"{iss_longitude}")
        break
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
