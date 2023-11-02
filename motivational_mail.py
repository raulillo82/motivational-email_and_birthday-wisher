import smtplib
import datetime as dt
from random import choice
from auth import *

QUOTES = "./quotes.txt"
SMTP_SERVER = "smtp.gmail.com"

try:
    with open(QUOTES) as quotes_file:
        quotes_list = quotes_file.readlines()
except FileNotFoundError:
    print(f"File {QUOTES} not found! Terminating the program.")
else:
    if dt.datetime.now().weekday() == 1: #Check for Mondays
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            quote = choice(quotes_list)
            msg = "Subject:Motivational mail of the week\n\n" + quote
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg=msg)
