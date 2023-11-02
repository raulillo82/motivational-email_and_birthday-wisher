import pandas
import smtplib
import datetime as dt
from random import randint

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
now_tuple = (now.month, now.day)

if now_tuple in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    person = birthdays_dict[now_tuple]
    letter_file = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(letter_file) as letter:
        content = letter.read()
        content = content.replace("[NAME]", person["name"])

# 4. Send the letter generated in step 3 to that person's email address.

    SMTP_SERVER = "smtp.gmail.com"

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        name = person["name"]
        msg = f"Subject:Happy birthday, {name}!\n\n{content}"
        connection.sendmail(from_addr=email, to_addrs=email, msg=msg)
