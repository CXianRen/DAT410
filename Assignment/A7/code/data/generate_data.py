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
        weather_data[date]="temperature: " + str(temperature) + " degrees, humidity: " + str(humidity) + "%, weather: " + weather
    return weather_data

import datetime


# city lists
cities = ['stockholm','gothenburg', 'malmo','uppsala','lund']

city_weather_data = {}
def init_weather_data():    
    start_date = datetime.date.today()
    for city in cities:
        city_weather_data[city] = generate_weather_data(datetime.date.today(), start_date + datetime.timedelta(days=14))
    return city_weather_data


def convert_date_to_datetime(date):
    date_map = {
    "today": 0,
    "tomorrow": 1,
    "2 days": 2,
    "two days": 2, # "two days" is same as "2 days"
    "3 days": 3,
    "three days": 3, # "three days" is same as "3 days
    "4 days": 4,
    "four days": 4, # "four days" is same as "4 days
    "5 days": 5,
    "five days": 5, # "five days" is same as "5 days
    "next week": 7,
    "that day": -1, # should be calculated
    "this weekend":  -1 # should be calculated
    }

    if date in date_map:
        return datetime.date.today() + datetime.timedelta(days=date_map[date])
    
    month_map = {
        "january": 1,
        "jan": 1, # "jan" is short for "january"
        "february": 2,
        "feb": 2, # "feb" is short for "february
        "march": 3,
        "mar": 3, # "mar" is short for "march
        "april": 4,
        "apr": 4, # "apr" is short for "april
        "may": 5,
        "june": 6,
        "jun": 6, # "jun" is short for "june
        "july": 7,
        "jul": 7, # "jul" is short for "july
        "august": 8,
        "aug": 8, # "aug" is short for "august
        "september": 9,
        "sep": 9, # "sep" is short for "september
        "october": 10,
        "oct": 10, # "oct" is short for "october
        "november": 11,
        "nov": 11, # "nov" is short for "november
        "december": 12,
        "dec": 12, # "dec" is short for "december
    }

    for key in month_map:
        if date.find(key) != -1:
            month = month_map[key]
            day = int(date.split(" ")[0])
            return datetime.date(datetime.date.today().year, month, day)
        
    if date in month_map:
        return datetime.date(datetime.date.today().year, month_map[date], 1)
    
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return date.date()
    except ValueError:
        return None
    

def get_weather_data(city, date):
    """
      return 1 if city is not in the list
      return 2 if date is not in the list
      return 3 if date is not in the correct format
      return weather data if city and date are in the list
    """
    
    date = convert_date_to_datetime(date)
    if date == None:
        return 3, None
    if city not in cities:
        return 1, None
    if date not in city_weather_data[city]:
        return 2, None
    return 0, city_weather_data[city][date]
    

city_restaurant_data = {}

def generate_restaurant_data(city):
    restaurant_data = {}
    for i in range(20):
        restaurant_name = city + " restaurant " + str(i)
        restaurant_data[restaurant_name] = {
            "food_type": random.choice(['chinese', 'italian', 'mexican', 'american']),
            "parking": random.choice(['yes', 'no']),
            "price": random.choice(['less than 100', '100-200', '200-300', 'more than 300']),
            "rating": random.randint(1, 5)
        }
    return restaurant_data

def init_restaurant_data():
    for city in cities:
        city_restaurant_data[city] = generate_restaurant_data(city)
    return city_restaurant_data

def get_restaurant_data(city, food_type = 'all', rating = 1, price= 'all'):
    """
      return 1 if city is not in the list
      return 2 if food_type is not in the list
      return 3 if price is not in the list
      return 4 if rating is not in the list
      return restaurant data if city and date are in the list
    """
    if city not in cities:
        print("\t\t\t\t[Debug]: can't find city:", city)
        return 1, None
    if food_type not in ['all', 'chinese', 'italian', 'mexican', 'american']:
        print("\t\t\t\t[Debug]: can't find food_type:", food_type)
        return 2, None
    if price not in ['all','less than 100', '100-200', '200-300', 'more than 300']:
        print("\t\t\t\t[Debug]: can't find price:", price)
        return 3, None
    if rating not in [1, 2, 3, 4, 5]:
        print("\t\t\t\t[Debug]: can't find rating:", rating)
        return 4, None
    print("\t\t\t\t[Debug]: get_restaurant_data city:", city)
    ret = []
    for restaurant in city_restaurant_data[city]:
        if city_restaurant_data[city][restaurant]["food_type"] == food_type or food_type == 'all':
            if city_restaurant_data[city][restaurant]["price"] == price or price == 'all':
                if city_restaurant_data[city][restaurant]["rating"] >= rating:
                    ret.append({restaurant: city_restaurant_data[city][restaurant]})
    # print("\t\t\t\t[Debug]: get_restaurant_data result:", ret)

    return 0, ret


# bus data
line_time_table = {}
line_time_table["1"] = {
    "stop11": ["8:00", "10:10", "12:20", "13:30", "14:40", "16:50", "18:00", "20:10", "22:20"],
    "stop12": ["8:10", "10:20", "12:30", "13:40", "14:50", "17:00", "19:10", "21:20", "23:30"],
    "stop13": ["8:20", "10:30", "12:40", "13:50", "15:00", "17:10", "19:20", "21:30", "23:40"],
}

line_time_table["2"] = {
    "stop21": ["9:00", "11:10", "13:20", "14:30", "15:40", "17:50", "20:00", "22:10", "24:20"],
    "stop22": ["9:10", "11:20", "13:30", "14:40", "15:50", "18:00", "20:10", "22:20", "24:30"],
    "stop23": ["9:20", "11:30", "13:40", "14:50", "16:00", "18:10", "20:20", "22:30", "24:40"],
}

line_time_table["3"] = {
    "stop31": ["10:00", "12:10", "14:20", "15:30", "16:40", "18:50", "21:00", "23:10", "25:20"],
    "stop32": ["10:10", "12:20", "14:30", "15:40", "16:50", "19:00", "21:10", "23:20", "25:30"],
    "stop33": ["10:20", "12:30", "14:40", "15:50", "17:00", "19:10", "21:20", "23:30", "25:40"],
}

def get_bus_data(line, stop):
    """
      return 1 if line is not in the list
      return 2 if stop is not in the list
      return 3 if time is not in the correct format
      return 0, t if line and stop are in the list, t is the most recent bus
    """
    time = datetime.datetime.now().strftime("%H:%M")
    print("\t\t\t\t[Debug]: get_bus_data line:", line, "stop:", stop, "time:", time)
    
    # find the most recent bus
    if line not in line_time_table:
        return 1, None
    if stop not in line_time_table[line]:
        return 2, None
    
    time_table = line_time_table[line][stop]
    for t in time_table:
        if t > time:
            return 0, t
    return 3, None

