#Begaye, Gamaliel
#10/30/2021
#Project-Connecting with a Weather API and display weather forcast with a interactive program. 
import requests
from requests.models import Response
import json
#User name input with Welcome message.
name = str(input("Please enter your name: "))
print(f"Welcome to today's weather forcast! {name}")
#This block of code connects with Weather API with input from the user and also closes the program. 
while True:
    weatherinput = str(input("Please enter the city or zipcode for the current weather forcast (input 'exit' if you want to exit the program: "))
    if weatherinput == 'exit': 
        break
    else:
        try:
           url = 'http://api.openweathermap.org/data/2.5/weather'
           querystring= {"zip": '{weatherinput}', "city": '{weatherinput}', "APPID": "53c798368addae7221fdac5143aa565d"}
           headers= { 'cache-control': "no-cache" }
           response = requests.request ("GET", url, headers=headers, params=querystring)
           print(response.text)
        except Exception as e:
            print(f"Error! {e}")
            pass 
#Make the JSON files into a readable format
    import json

    response.json()