'''
Model for JSON input/output operations.
I've defined 2 internal functions for reading and writing to JSON files
and 6 external functions for reading and writing to specific JSON files
Use the external functions in your main code.

from jsonio import read_books, read_cakes, read_drinks, write_books, write_cakes, write_drinks
'''

# Imports
import json

# Write to JSON file - INTERNAL USE ONLY
# Takes file name and dictionary to write as parameters
# Read existing data, update with new data, and write back to file
def write_to_json(file_name, write_data):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(write_data)

    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data written to {file_name}")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

# Read from JSON file - INTERNAL USE ONLY
# Return data as a dictionary
def read_from_json(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return None
    except Exception as e:
        print(f"Error reading from JSON file: {e}")
        return None

# Read from specific JSON files - EXTERNAL USE ONLY
# Return data as a dictionary
def read_books():
    books = read_from_json('books.json')
    return books

def read_cakes():
    cakes = read_from_json('cakes.json')
    return cakes

def read_drinks():
    drinks = read_from_json('drinks.json')
    return drinks

# Write to specific JSON files - EXTERNAL USE ONLY
# Takes dictionary to write as parameter
def write_books(data):
    write_to_json('books.json', data)

def write_cakes(data):
    write_to_json('cakes.json', data)

def write_drinks(data):
    write_to_json('drinks.json', data)
