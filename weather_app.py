from logging import root
from struct import pack
import requests
import json
from tkinter import *
from datetime import datetime

'''We first initialize the GUI window
along with the window's default size and the title of our window'''

root = Tk()
root.geometry("500x500")
#this makes the size of the window fixed
root.resizable(0,0)
root.title("Weather App - AskPython.com")

city_value=StringVar()

'''This function displays the weather'''
def display_weather():
    #the api key from the OpenWeatherMap dashboard
    api_key= "b88de5a8b401de899d97e67c091d94b0"
    #get city name from the user form code later in the code
    city_name = city_value.get()
    weather_url = "https://openweathermap.org/api" + city_name + '&appid' +api_key
    #get the response from the fetched url
    response = requests.get(weather_url)
    #here we are changing the json response to python readable
    weather_information =response.json()
    #this clears the text field for a new output
    tfield.delete("1,0","end")

    if weather_information['cod']==200:
        kelvin = 273
        # storing the fetched values of the city's weather
        pressure = weather_information["main"]['pressure']
        wind_speed =weather_information['wind']['speed']
        timezone = weather_information['timezone']
        feels_like= int(weather_information['main']['feels_like'] -kelvin)
        temperature= int(weather_information['main']['temperature'])
        humidity = weather_information['main']['humidity']
        cloudy = weather_information['cloudy']['all']
        sunset = weather_information['sys']['sunset']
        sunrise= weather_information['sys']['sunrise']
        description = weather_information['weather'][0]['description']

        sunrise_time = timezone_format_for_location(sunrise + timezone)
        sunset_time = timezone_format_for_location(sunset + timezone)

        #assigning the values of our weather variables to display as output
        degree_sign = u'\N{DEGREE SIGN}'
        weather = f'\nWeather of: {city_name}\nTemperature (Celsius): {temperature}{degree_sign}\nFeels like (Celsius): {feels_like}{degree_sign}\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunrise at {sunset_time}\nCloud: {cloudy}%\nInfo : {description}'
    else:
        weather = f'\n\tWeather of: {city_name} not found!\n\tKindly enter a valid City name.'

    #to insert or send values in our text field to display as out
    tfield.insert(INSERT,weather)

def timezone_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

city_head = Label(root, text= "Enter city name", font= 'Arial 12 bold').pack(pady=10)
#entry field 
inp_city= Entry(root, textvariable= city_value, width= 24 ,font='Arial 12 bold').pack()
Button(root, command = display_weather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

#to show output
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()