import requests
from pprint import pprint

city = input("What city weather you like me to check? : ")

APIKEY = '6f5aec165df1a00cd2698d82f467fbd4'

base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + APIKEY + '&q=' + city

data = requests.get(base_url).json()

pprint(data)