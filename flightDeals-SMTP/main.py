import requests
from smtplib import *
from datetime import *
from dateutil.relativedelta import *

api_key = 'YOUR_API_KEY'
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
my_email = 'YOUR_EMAIL'
password = 'PASSWORD'

sheety_endpoint = 'https://api.sheety.co/b92cd03a1abe1e5baea51d691366a176/flightDeals/prices'
new_endpoint = 'https://api.sheety.co/b92cd03a1abe1e5baea51d691366a176/flightDeals/users'
tequila_endpoint = 'https://tequila-api.kiwi.com/v2/search'

tequila_header = {
    "apikey": api_key
}

sheety_header = {
    "Content-Type": "application/json",
}

sheety_response = requests.get(url=sheety_endpoint)
sheet_data = sheety_response.json()
prices = sheet_data['prices']

tomorrow = date.today() + relativedelta(days=1)
tomorrow = tomorrow.strftime('%d/%m/%Y').replace("-", "/")
six_months = date.today() + relativedelta(months=+6)
six_months = six_months.strftime('%d/%m/%Y').replace("-", "/")

first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
email_first = input("Enter your email address: ")
email_second = input("Enter your mail address again: ")

user_deets = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email_first
    }
}

if email_first == email_second:
    response = requests.post(url=new_endpoint, json=user_deets, headers=sheety_header)
    print("You've been successfully added to the list!")

    for i in range(len(prices)):
        code = sheet_data['prices'][i]['iataCode']
        params = {
            "fly_from": "LON",
            "fly_to": f"{code}",
            "dateFrom": f"{tomorrow}",
            "dateTo": f"{six_months}",
            "curr": "GBP"
        }
        response = requests.get(url=tequila_endpoint, headers=tequila_header, params=params)
        tequila_data = response.json()

        for dictionary in prices:
            if tequila_data['data'][i]['price'] < dictionary['lowestPrice']:
                from_place = tequila_data['data'][i]['flyFrom']
                to_place = tequila_data['data'][i]['flyTo']
                to_city = tequila_data['data'][i]['cityTo']
                offer_price = tequila_data['data'][i]['price']
                mail_address = user_deets['user']['email']
                receiver = user_deets['user']['firstName']
                with SMTP('smtp.gmail.com') as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=mail_address,
                                        msg=f"Subject:Low flight deals! ✈️\n\n"f"Hey {receiver} 👋\n"
                                            f"Low price alert 💰! Only £{offer_price} to fly from London-{from_place} "
                                            f"to {to_city}-{to_place}.".encode('utf-8'))
else:
    print("Please check your Email again!")
