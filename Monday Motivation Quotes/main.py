import smtplib
import datetime as dt
import random as r

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

with open("quotes.txt") as q:
    quotes = q.read().splitlines()
day = dt.datetime.now().weekday()
# hour = dt.datetime.now().hour
if day == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="YOUR FRIEND EMAIL",
            msg=f"Subject:Feliz Lunes!\n\n{r.choice(quotes)}")
# If you want to send to a lot of people, you should repeat the connection.sendmail() with your email list