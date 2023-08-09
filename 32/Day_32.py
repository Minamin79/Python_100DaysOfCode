import smtplib
import datetime as dt
import pandas
import random


birthday_data = pandas.read_csv("birthdays.csv")             #Enter your data in the csv file
birthday_dict = birthday_data.to_dict(orient="records")

now = dt.datetime.now()
name_text = "[NAME]"

for entry in birthday_dict:
    if entry["month"] == now.month and entry["day"] == now.day:
        letter_num = random.randint(1, 3)
        name = entry["name"]
        email = entry["email"]
        with open(f"letter_templates/letter_{letter_num}.txt", mode="r") as letter_file:
            draft_letter = letter_file.read()
            birthday_letter = draft_letter.replace(name_text, name)


my_email = "@gmail.com"                                      #Enter your gmail here
password = ""                                                #Enter your password here
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=f"{email}",
        msg=f"Subject:HBD\n\n{birthday_letter}"
    )