import json
import smtplib
import requests
# ------------ Email -------------#
my_email = " "
send_to = " "
password = " "

# ------------ API ------------- #
api_key = " "
api_url = "http://api.openweathermap.org/data/2.5/weather?q=Jaipur,India&APPID=bf8f38b6df121ed81f80df037c1e6e8b"
one_call_url = "https://api.openweathermap.org/data/2.5/onecall"
parameter = {
    "lat": 26.9167, "lon": 75.8167,
    "units": "metric",
    "exclude": "current,daily,minutely",
    "appid": " "
}
response = requests.get(url=one_call_url, params=parameter)
response.raise_for_status()

weather_data = response.json()
hourly_weather = weather_data["hourly"]

_12_hour_weather = []
umbrella_needed = False
# for i in range(12):
#     if hourly_weather[i]['weather'][0]["id"] < 800:
#         umbrella_needed = True
#     _12_hour_weather.append(hourly_weather[i]['weather'][0])
_12_hour_weather = hourly_weather[:12]

for i in _12_hour_weather:
    if i['weather'][0]['id'] < 700:
        umbrella_needed = True

umbrella_needed = True
if umbrella_needed:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=send_to, msg=f"Subject: Bring an Umbrella\n\n"
                                                                               f"Message from python program")
        print("mail send")
        connection.close()


print(_12_hour_weather)
