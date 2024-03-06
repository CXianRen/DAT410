import spacy
import re
from data.generate_data import *
import datetime

init_weather_data()
init_restaurant_data()

def clean_text(text):
  text = re.sub(r'\s+', ' ', text)
  text = text.strip().lower()
  return text

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def city_parser(doc):
  for ent in doc.ents:
    if ent.label_ == "GPE":
      return ent.text
  return None

def date_parser(doc):
  for ent in doc.ents:
    if ent.label_ == "DATE":
      return ent.text
  return None

def food_type_parser(doc):
  # just a simple example, you can use a more complex model to parse the food type
  for token in doc:
    if token.text in ["chinese", "italian", "mexican", "american", "french", "indian", "thai", "japanese"]:
      return token.text
  return None

def price_parser(doc):
  # just a simple example, you can use a more complex model to parse the price
  for token in doc:
    if token.text in ["cheap", "expensive", "moderate", "pricey", "affordable", "budget", "price"]:
      return token.text
  return None

def rating_parser(doc):
    # just a simple example, you can use a more complex model to parse the rating
  for token in doc:
    if token.text in ['rate', 'rating', 'stars', 'star', 'score', 'scores']:
        # return the next token
      return doc[token.i+1].text
  return None

def line_parser(doc):
    for token in doc:
        if token.text in ["line", "lines"]:
            return doc[token.i+1].text
    return None

def stop_parser(doc):
    for token in doc:
        if token.text in ["stop", "station", "stations"]:
            return doc[token.i+1].text
    return None

parser_map = {
  "city_parser": city_parser,
  "date_parser": date_parser,
  "get_weather_data": get_weather_data,
  "food_type_parser": food_type_parser,
  "price_parser": price_parser,
  "rating_parser": rating_parser,
  "get_restaurant_data": get_restaurant_data,
  "line_parser": line_parser,
  "station_parser": stop_parser,
  "get_bus_data": get_bus_data
}


WeatherFrame = {
  "slots":[
     # slot 1
    {
      "slot_name": "city",
      "slot_value": -1,
      "question": "What city do you want to know the weather for?",
      "parser": "city_parser",
      "fail_response": "I'm sorry, I don't know the weather for that city. Please try again.",
    },
    # slot 2
    {
      "slot_name": "date",
      "slot_value": -1,
      "question": "What date do you want to know the weather for?",
      "parser": "date_parser",
      "fail_response": "I'm sorry, I don't know the weather for that date. Please try again.",
    }
  ],
  "output_template":  {
      "template": "The weather in {} on {} is {}.",
      "params": ["city", "date", "ret"]
    },
  
  "general_fail_response": "I'm sorry, I don't know the weather for that city or date. Please try again.",
  "cmd": "get_weather_data"
}

ResturantFrame = {
  "slots":[
    # slot city
    {
      "slot_name": "city",
      "slot_value": -1,
      "question": "What city do you want to know the restaurants for?",
      "parser": "city_parser",
      "fail_response": "I'm sorry, I don't know the restaurants on that city. Please try again.",
    },
    # slot type 
    {
      "slot_name": "food_type",
      "slot_value": "all", # food_type: all, chinese, italian, mexican, american
      "question": None, # when slot_value with default value, 
                        # it means the slot is optional, won't ask the user proactively
      "parser": "food_type_parser",
      "fail_response": None,

    },
    # slot rating
    {
      "slot_name": "rating",
      "slot_value": 1, # rating: all, 1, 2, 3, 4, 5
      "question": None, # when slot_value with default value, 
                        # it means the slot is optional, won't ask the user proactively
      "parser": "rating_parser",
      "fail_response": None,
    },
  ],
  "output_template": {
      "template": "the perfect restaurant for you in {} are: {}.",
      "params": ["city", "ret"]
    },
  
  "general_fail_response": "I'm sorry, I cannot find the restaurants for that city. Please try again.",
  "cmd": "get_restaurant_data"
}

BusFrame = {
  "slots":[
     # slot 1
    {
      "slot_name": "line",
      "slot_value": -1,
      "question": "which line do you want to know check?",
      "parser": "line_parser",
      "fail_response": "I'm sorry, I can't not find the information about this line. Please try again.",
    },
    # slot 2
    {
      "slot_name": "start_station",
      "slot_value": -1,
      "question": "which station you start?",
      "parser": "station_parser",
      "fail_response": "I'm sorry, I can't not find the information about this station. Please try again.",
    }
  ],
  "output_template":  {
      "template": "The next bus start from {} is {}.",
      "params": ["start_station", "ret"]
    },
  
  "general_fail_response": "I'm sorry, I can't not find the information about this line and station. Please try again.",
  "cmd": "get_bus_data"
}



topic_frame_map = {
    # 0 
    0: ["weather", "rain", "temperature", "forecast", "snow"],
    1: ["restaurant", "food", "eatery", "eat", "dinner", "lunch", "breakfast", "recommend"],
    2: ["bus", "line", "station", "stop", "bus stop", "bus station", "bus lines"]
}

def check_topic(sentence):
    #print("\t\t\t\t[Debug]: sentence:", sentence)
    for i in range(len(topic_frame_map)):
        for word in topic_frame_map[i]:       
            if sentence.find(word) != -1:
                #print("\t\t\t\t[Debug]: word:", word)
                return i
    return -1


from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def simple_conversation(sentence):
    mdict={
        "hello": "Hi, I'm a travel bot, you can ask me about the weather, resuturants and buses!, Or Say 'goodby' to exit.",
        "goodby": "Goodby!",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!",
        "thank you very much": "You're welcome!",
        "thank you so much": "You're welcome!",
        "thank you a lot": "You're welcome!",
        "can you help me": "Sure, I can help you with the weather, resuturants and buses!",
        "hi": "Hi, I'm a travel bot, you can ask me about the weather, resuturants and buses!, Or Say 'goodby' to exit.",
        "bye": "Goodby!",
    }
    for key in mdict:
        if similar(key, sentence) > 0.7:
            #print("\t\t\t\t[Debug]: similar:", key, sentence, similar(key, sentence))
            return mdict[key]
    return None



import copy

def _run_chatbot():
    conversation_round = 0
    # print("[Talking Round]:", conversation_round)
    print("Bot: Hi, I'm a travel bot, you can ask me about the weather, resuturants and buses!, Or Say 'goodby' to exit.")
    frame = None
    ctopic = -1
    i = 0
    while True:
        # read user input and process it
        sentence = input("You:")
        print("")
        sentence = clean_text(sentence)
        doc = nlp(sentence)
        # check if the user want to exit
        if sentence == "goodby":
            print("Bot: Goodby!")
            break

        # check topic
        topic = check_topic(sentence)
        #print("\t\t\t\t[Debug]: ttopic:", topic)
        if topic == -1:
            # simple conversation
            ret = simple_conversation(sentence)
            if ret:
                print("Bot:", ret)    
                continue
            else:
                if ctopic == -1:
                    print("Bot: I'm sorry, I don't understand what you are talking about.")
                    continue
            

        # check if the user want to change topic
        if ctopic != topic and topic != -1:
            ctopic = topic
            if ctopic == 0:
                frame = copy.deepcopy(WeatherFrame)
            elif ctopic == 1:
                frame = copy.deepcopy(ResturantFrame)            
            elif ctopic == 2:
                frame = copy.deepcopy(BusFrame)
            else:
                print("Bot: I'm sorry, I don't understand what you are talking about.")
                continue


    
        # fill the slot    
        # every time we try to fill all slot. 
        for j in range(len(frame["slots"])):
            slot = frame["slots"][j]
            parser = parser_map[slot["parser"]]
            slot_value = parser(doc)
            if slot_value:
                #print("\t\t\t\t[Debug]: slot_key(%s):slot_value(%s)"% (slot['slot_name'], slot_value))
                frame["slots"][j]["slot_value"] = slot_value

        # check if the current slot was filled.
        for i in range(len(frame["slots"])):
            if frame["slots"][i]["slot_value"] == -1:
                # proactively ask the user
                conversation_round+=1
                # print("[Talking Round]:", conversation_rouand)
                print("Bot:",frame["slots"][i]["question"])
                break
            else:
                # check next slot
                i += 1
        
        if i >= len(frame["slots"]):
            # break we don't break the loop, just give the answer and continue until the user say "goodby"
            #print("\t\t\t\t[Debug]: All slots are filled")
            #print("\t\t\t\t[Debug]: slots:", [slot["slot_name"] + ":"+ str(slot["slot_value"]) + ";" for slot in frame["slots"]])
                    # get the weather data
            paramers = ()
            for slot in frame["slots"]:
                paramers += (slot["slot_value"],)
            ret_code, ret = parser_map[frame["cmd"]](*paramers)
            if ret:
                format_params = ()
                for p in frame["output_template"]["params"]:
                    for slot in frame["slots"]:
                        if slot["slot_name"] == p:
                            format_params += (slot["slot_value"],)
                if frame["output_template"]["params"][-1] == "ret":
                    format_params += (ret,)
                print("Bot:", frame["output_template"]["template"].format(*format_params))
            else:
                print("Bot:", frame["general_fail_response"])

if __name__ == "__main__":
    _run_chatbot()
