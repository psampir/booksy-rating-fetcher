import requests
import json
import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup

if len(sys.argv) > 2: # if more than 1 argument provided
    print("Error: Too many arguments provided.")
    exit()
elif len(sys.argv) == 2: # if 1 argument provided
  path_to_file = sys.argv[1] # load path to data file from the argument
else: # if no arguments provided
  path_to_file = './rating.json'

path_to_file = os.path.expanduser(path_to_file) # expand the ~ in the path

url = 'https://booksy.com/pl-pl/99537_salon-urody-abacosun-ostrow-wielkopolski_salon-kosmetyczny_17258_ostrow-wielkopolski'
response = requests.get(url) # send a GET request to the server
soup = BeautifulSoup(response.content, 'html.parser') # parse the HTML content of the page

average_rating_element = soup.find('div', {'data-testid': 'rank-average'}) # find the element with the average rating
total_reviews_element = soup.find('div', {'data-testid': 'rank-label'}) # find the element with the reviews count

average_rating = None
total_reviews = None

date_of_data_fetch = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if total_reviews_element:
    total_reviews = total_reviews_element.text.strip()  # extract the text from the element
    total_reviews = total_reviews.split(' ')[0] # get only the number of reviews
    print(f"Total reviews:\t{total_reviews}")
else:
    print("Error: Did not find the `total_reviews` element.")
    exit()

if average_rating_element:
    average_rating = average_rating_element.text.strip()
    average_rating = average_rating.replace(',', '.') # replace , with . in the rating
    print(f"Average rating:\t{average_rating}")
else:
    print("Error: Did not find the `average_rating` element.")
    exit()

data = { # Save the data to JSON file
    'average_rating': average_rating,
    'total_reviews': total_reviews,
    'date_of_data_fetch': date_of_data_fetch
}

with open(path_to_file, 'w') as file:
    json.dump(data, file) # write the data to the file

print("Data saved to", path_to_file)