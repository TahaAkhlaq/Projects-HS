from twilio.rest import Client
import os
import requests
import schedule
import time

api_key = '74bdf834d029807bf75cfe0503b0e2e7'
user_input = input("City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")



account_sid = 'ACdbc09461abb49b6f845eb6b9327ebf76'
account_token = '3ab014fca25bb409b04280e9882f3060'
client = Client(account_sid, account_token)

message = client.messages.create(
        message = messaging_service_sid='MGa30159f8244a7011a3173c6e3db8a1cb',
        to='+13475569525',
        body=f"The weather in {user_input} is: {weather} and the temperature is: {temp}ºF",
)
print(message.sid),
   

schedule.every().day.at("01:22").do()

while True:
    schedule.run_pending()
    time.sleep(1)






 

