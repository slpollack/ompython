
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_restaurants(city, term):

	auth = Oauth1Authenticator(
	    consumer_key = os.environ["CONSUMER_KEY"],
	    consumer_secret= os.environ["CONSUMER_SECRET"],
	    token = os.environ["TOKEN"],
	    token_secret = os.environ["TOKEN_SECRET"]
	)
	
	client = Client(auth)

	params = {
    'term': term,
    'lang': "en"}
	

	response = client.search(city, **params)

	businesses = []	

	for business in response.businesses:
		businesses.append({"bizname": business.name, "bizrating":business.rating})

	return businesses





businesses =  get_restaurants("NYC", "food")



print(businesses)