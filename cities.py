import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from tqdm import tqdm
from tqdm.notebook import tqdm_notebook
import newspaper
import json
import datetime
import jsonpickle
import nltk
from newspaper import news_pool
from newspaper import Source
from newspaper import Config
from time import sleep
from json import JSONEncoder
import wikipedia


file = open('list_cities_US.txt','r')
all_cities =  []
ALL_CITIES = []
dict_cities = {}

for i in file.readlines():
	all_cities.append(i)
for city in all_cities:
	temp = city.replace('\n','')
	ALL_CITIES.append(temp)


state_abbrevs = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

state_names = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

for abbrev in state_abbrevs:
	
	abbrev_cities = []
	
	for city in ALL_CITIES:
		if abbrev in city:
			temp = city.split(',')[0]
			abbrev_cities.append(temp)

	dict_cities[str(abbrev)] = abbrev_cities



json_data = json.dumps(dict_cities, indent = 4, ensure_ascii=False)

with open("cities.json", "w") as outfile:
    outfile.write(json_data)


x = 0
notable_people = {}
for state in dict_cities:
	notable_people[state_names[x]] = {}
	x += 1

y = 0
for state in state_abbrevs:
	notable_people[state_names[y]] = {}
	for city in dict_cities[state]:
		notable_people[state_names[y]][city] = []
	y += 1


ii = 0

for state in notable_people:
	print("Finding people from " + str(state))
	for city in notable_people[state]:
		try:
			wiki = wikipedia.page(str(city) + ',' + str(state))
			people = []
			if '== Notable people ==' in str(wiki.content):
				temp = str(wiki.content).split("== Notable people ==")[1]
				temp2 = temp.split("=")[0]
				if temp2 == "":
					pass
				else:
					temp3 = temp2.strip()
					
					for line in temp3.splitlines():
			
						people.append(line)
			
			if people == []:
				if requests.get("https://en.wikipedia.org/wiki/List_of_people_from_" + str(city) + ",_" + str(state)).status_code != 200:
					continue
				wiki2 = wikipedia.page('List of people from ' + str(city) + ',' + str(state))


				temp3 = str(wiki2.content).splitlines()
				for line in temp3:
					if line == '':
						continue
					if '=' in line:
						continue
					if 'The following is a list of people' in line:
						continue
					else:
						people.append(line)

				people.pop()
				people.pop(0)
		except:
			pass


		notable_people[str(state)][city] = people

		json_data2 = json.dumps(notable_people, indent = 4, ensure_ascii=False)

		with open("people.json", "w") as outfile:
			outfile.write(json_data2)

