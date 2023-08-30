import requests
import datetime as dt
from twilio.rest import Client
import random as r
import smtplib

# Enterprise Data
STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

# Twilio Data Account
ACCOUNT_SID = "Twilio Account SID"
AUTH_TOKEN = "Twilio Account Token"

# Email Data Account
my_email = "Your Email"
password = "Your Password"

# API Constant
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

yt = str(dt.datetime.now().date() - dt.timedelta(days=1))
bf_yt = str(dt.datetime.now().date() - dt.timedelta(days=2))

stock_parameters = {
    "apikey": "Your API Key",
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": "Your API Key",
    "from": bf_yt,
    "to": yt,
    "language": "en",
    "sort_by": "relevancy"
}
up_down = None
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_data_bf_yt = stock_data["Time Series (Daily)"][bf_yt]
stock_data_yt = stock_data["Time Series (Daily)"][yt]
difference = float(stock_data_bf_yt["4. close"]) - float(stock_data_yt["4. close"])
close_df_percentage = round((difference / float(stock_data_yt["4. close"])) * 100, 2)

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
all_articles = [{"title": art["title"], "description": art["description"], "url": art["url"]} for art in
                news_data["articles"][0:3]]
if close_df_percentage >= 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# ------------------------------------- With SMTP Email Protocol -----------------------------------------

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     random_new = r.randint(0, 2)
#     message = f"""Subject:{COMPANY_NAME} Stock!\n"
#         {STOCK}: {up_down} {close_df_percentage}%
#         Headline: {all_articles[random_new]["title"]}
#         Brief: {all_articles[random_new]["description"]}
#         Do you wanna keep reading? Here is the source!
#         {all_articles[random_new]["url"]}"""
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="email",
#         msg=message.encode("utf-8")
#     )

# ------------------------------------- With Twilio --------------------------------------------------------
# client = Client(ACCOUNT_SID, AUTH_TOKEN)
# random_new = r.randint(0, 2)
# message = client.messages \
#     .create(
#     body=f""""
#     {STOCK}: {up_down}{close_df_percentage}%
#     Headline: {all_articles[random_new]["title"]}
#     Brief: {all_articles[random_new]["description"]}
#     Do you wanna keep reading? Here is the source!
#     {all_articles[random_new]["url"]}
#     """,
#     from_='Your Twilio Number',
#     to='A Verified Number'
# )
