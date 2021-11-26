from smtplib import *
from datetime import *
import random

my_email = '***************@gmail.com'
my_password = '***********'

current_day = datetime.today().weekday()

if current_day == 0:
    with open('quotes.txt') as file:
        quote_data = file.readlines()
        random_quote = random.choice(quote_data)
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="*************@gmail.com",
                            msg=f"Subject:Some Monday motivation\n\n"f"It's the start of a new week!\n{random_quote}\nGood day!")
else:
    with open('quotes.txt') as file:
        quote_data = file.readlines()
        random_quote = random.choice(quote_data)
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="**************@gmail.com",
                            msg=f"Subject:Today's quote!\n\n"f"\n{random_quote}\nGood day!")
