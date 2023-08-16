import smtplib
import pandas as p
import datetime as dt
import random as r

MY_EMAIL = "YOUR GMAIL"
PASSWORD = "YOUR PASSWORD"
TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_data = p.read_csv("birthdays.csv")
birthday_dict = {(row["month"], row["day"]): (row["name"], row["email"]) for index, row in birthday_data.iterrows()}

now = dt.datetime.now()
day = now.day
month = now.month

if (month, day) in birthday_dict:
    name, email = birthday_dict[(month,day)]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        with open(f"letter_templates/{r.choice(TEMPLATES)}") as letter:
            new_letter = letter.read()
            new_letter = new_letter.replace("[NAME]", f"{name}")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday {name}!\n\n{new_letter}")

