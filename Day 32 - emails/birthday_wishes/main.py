##################### Hard Starting Project ######################
import smtplib

import pandas
import datetime as dt
import random
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
PLACEHOLDER = "[NAME]"
MY_EMAIL = ""
MY_PASSWORD = ""

# 2. Check if today matches a birthday in the birthdays.csv
today_datetime = dt.datetime.now()
today_tuple = (today_datetime.month, today_datetime.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person["name"])  # Needs to save into a variable
        with open(f"email_for_{birthday_person['name']}.txt", 'w') as new_letter:
            new_letter.write(contents)

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=birthday_person["email"],
    #         msg=f"Subject: Happy Birthday! \n\n{contents}"
    #     )






