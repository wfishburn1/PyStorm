# Helper functions - what are they?
# small, niche functions that perform very specific tasks

# Think supplement, not core

# Math operations
from datetime import datetime
import random

def calc_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Reading and Writing of files
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Coversion
def inches_to_cm(inches):
    return inches * 2.54

def lbs_to_kg(pounds):
    return pounds * 0.453592

# Date and Time
def get_date():
    return datetime.now().date()

def date_fmt(date):
    return date.strftime("%Y-%m-%d")

current_date = get_date()
formatted_date = date_fmt(current_date)
print(f"Current Date: {current_date}")
print(f"Formatted Date: {formatted_date}")

inches_value = 47.5
centimeter_value = inches_to_cm(inches_value)
print(f"{inches_value} inches is equal to {centimeter_value:.2f} centimeters.")

def gen_rand_num():
    return random.randint(1, 1000)

random_num = gen_rand_num()
print(f"Random Number: {random_num}")