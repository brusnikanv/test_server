import requests

def weather_city():
    city_name = request.args.get('city')
    days = request.args.get('days')
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {'key': '8cb0aaf915854606bf9105858202309',
              'q': city_name,
              'format': 'json',
              'num_of_days':days,
              'lang':'ru'}

    result = requests.get(weather_url, params=params)
    weather = result.json()
    return weather
if __name__ == '__main__':
    weather_city()