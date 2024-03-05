# generate weather data

# generate weather data for 14 days

import random
random.seed(10)

def generate_weather_data(start_date, end_date):
    weather_data = {}
    for i in range(14):
        date = start_date + datetime.timedelta(days=i)
        temperature = random.randint(10, 40)
        humidity = random.randint(10, 90)
        weather = random.choice(['sunny', 'rainy', 'cloudy'])
        weather_data[date]=(temperature, humidity, weather)
    return weather_data

import datetime


# city lists
cities = ['Stockholm','Gothenburg', 'Malmo','Uppsala','Lund']

city_weather_data = {}
def init_weather_data():    
    start_date = datetime.date.today()
    for city in cities:
        city_weather_data[city] = generate_weather_data(datetime.date.today(), start_date + datetime.timedelta(days=14))
    return city_weather_data

def get_weather_data(city, date):
    """
      return 1 if city is not in the list
      return 2 if date is not in the list
      return weather data if city and date are in the list
    """
    if city not in cities:
        return 1, None
    if date not in city_weather_data[city]:
        return 2, None
    return 0, city_weather_data[city]