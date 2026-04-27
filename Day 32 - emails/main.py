# SMTP (Simple Mail Transfer Protocol)
import smtplib

my_email = ""
password = ""

# GMAIL: smtp.gmail.com
# HOTMAIL: smtp.office365.com
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Secure connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Subject: Hello\n\n This is the body of my email"
    )

# =========================================== #
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1995, month=12, day=14)

if day_of_week == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        line = random.choice(all_quotes)
    print(line)