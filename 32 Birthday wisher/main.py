import datetime as dt
import smtplib
import pandas
import random

my_email = "yashdhakade1234@gmail.com"
password = "nsfqbuydlyxsxgup"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    birthday_person = birthday_dict[today]
    # print(person_name)
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"subject: Happy Birthday!\n\n{contents}")
