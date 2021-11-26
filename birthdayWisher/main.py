from datetime import *
from smtplib import *
import os
import pandas
import random

current_month = datetime.now().month
current_day = datetime.now().day

my_email = '*******************@gmail.com'
password = '**************'

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient='records')
print(birthday_dict)

for birthday in birthday_dict:
    if birthday['month'] == current_month and birthday['day'] == current_day:
        birthday_person = birthday['name']
        birthday_mail = birthday['email']
        letters = os.listdir(<absolute file path>)
        random_letter = random.choice(letters)

        with open(f"./letter_templates/{random_letter}") as greetings:
            letter = greetings.read()
            letter = letter.replace("[NAME]", birthday_person)
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_mail,
                                msg=f"Subject:Happy birthday {birthday_person}!\n\n{letter}"
                                )


