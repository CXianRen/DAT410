import spacy

from data.generate_data import *
from chatbot import *

sentence= clean_text("What is the weather in Gothenburg today?")

assert city_parser(nlp(sentence)) == "gothenburg", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg tomorrow?")
assert date_parser(nlp(sentence)) == "tomorrow", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg the day after tomorrow?")
assert date_parser(nlp(sentence)) == "the day after tomorrow", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg in 3 days?")

assert date_parser(nlp(sentence)) == "3 days", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg in three days?")
assert date_parser(nlp(sentence)) == "three days", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg on Jun 1st?")
assert date_parser(nlp(sentence)) == "jun 1st", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg on that day?")
assert date_parser(nlp(sentence)) == "that day", "Test failed!"

sentence= clean_text("What is the weather in Gothenburg this weekend?")
assert date_parser(nlp(sentence)) == "this weekend", "Test failed!"

# test data conversion
assert convert_date_to_datetime("today") == datetime.date.today(), "Test failed!"
assert convert_date_to_datetime("tomorrow") == datetime.date.today() + datetime.timedelta(days=1), "Test failed!"
assert convert_date_to_datetime("2 days") == datetime.date.today() + datetime.timedelta(days=2), "Test failed!"
assert convert_date_to_datetime("three days") == datetime.date.today() + datetime.timedelta(days=3), "Test failed!"
assert convert_date_to_datetime("four days") == datetime.date.today() + datetime.timedelta(days=4), "Test failed!"
assert convert_date_to_datetime("five days") == datetime.date.today() + datetime.timedelta(days=5), "Test failed!"
assert convert_date_to_datetime("next week") == datetime.date.today() + datetime.timedelta(days=7), "Test failed!"
# assert convert_date_to_datetime("that day") == -1, "Test failed!"


# food_type parser
sentence= clean_text("can you recommend any good Chinese restaurants?")
assert food_type_parser(nlp(clean_text(sentence))) == "chinese", "Test failed"

sentence= clean_text("Do you have any suggestions for Italian restaurants?")
assert food_type_parser(nlp(clean_text(sentence))) == "italian", "Test failed"

sentence= clean_text("any recommendations for a great Indian eatery?")
assert food_type_parser(nlp(clean_text(sentence))) == "indian", "Test failed"

