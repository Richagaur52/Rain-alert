import requests
from twilio.rest import Client

OWN_Endpoint="https://api.openweathermap.org/data/2.5/weather"
api_key="2e118fa72cec2eee569839af442c6061"
account_sid = 'AC251f8d93de93588daa7dd1c945640a4b'
auth_token = 'de7d7821023941be09bbb6aa24e3b6c8'

weather_prams={
    "lat":35.689487,
    "lon": 139.691711,
    "appid":api_key
}
response=requests.get(OWN_Endpoint,params=weather_prams)
weather_info=response.json()
more_info=weather_info['weather']
# print(more_info)
weather_detail=int(more_info[0]['id'])
if weather_detail<700:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG7fdf6f48d98aeddd5163df89908268df',
        body='It\'s raining outside.Do not forget to take Umbrella.Have a good day!',
    to = '+916398243156'
    )
    # print(message.sid)
    print(message.status)
    # print(f"Take umbrella,it's {more_info[0]['main']} outside.Have a good day!")
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MG7fdf6f48d98aeddd5163df89908268df',
        body='It\'s clear outside.Have a good day!',
        to='+916398243156'
    )
    # print(message.sid)
    print(message.status)
    # print(f"It's {more_info[0]['main']} outside.Have a good day!")

