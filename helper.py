import json
import wikipedia
import requests
from tqdm import tqdm


# f = open('people_copy.json',)

# data = json.load(f)
# no_cities  = []
# one_cities = []
# recheck_cities_one = []
# recheck_cities_none = []
# for state in data:
# 	print("Checking " + state)
# 	for city in tqdm(data[state]):
		
# 		if len(data[str(state)][str(city)]) == 1:
# 			one_cities.append(str(city + ", " + state))

# 			try:
# 				if "notable" in data[str(state)][str(city)][0]:
# 					recheck_cities_one.append(str(city) + ", " + str(state))
# 					continue
# 				if requests.get("https://en.wikipedia.org/wiki/List_of_people_from_" + str(city) + ",_" + str(state)).status_code != 200:
# 					continue
# 				else:
# 					recheck_cities_one.append(str(city) + ", " + str(state))
# 			except:
#  				pass
 		
 		
# 		elif len(data[str(state)][str(city)]) == 0:
# 			no_cities.append(str(city + ", " + state))

# 			try:
# 				if requests.get("https://en.wikipedia.org/wiki/List_of_people_from_" + str(city) + ",_" + str(state)).status_code != 200:
# 					continue
# 				else:
# 					recheck_cities_none.append(str(city) + ", " + str(state))
# 			except:
# 				pass
# 	print("Cities with no people: " + str(len(no_cities)))
# 	print("Blank Cities with a wikipedia page: " + str(len(recheck_cities_none)))
# 	print("-----------------------------------------------------")
# 	print("Cities with only one line: " + str(len(one_cities)))
# 	print("One Liners with a wikipedia page: " + str(len(recheck_cities_one)))


# print(recheck_cities_one)
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(recheck_cities_none)


# a = ['Bloomfield Hills, Michigan', 'Lincoln, Nebraska', 'Las Vegas, Nevada', 'Trenton, New Jersey', 'Albuquerque, New Mexico', 'New Rochelle, New York', 'Fargo, North Dakota', 'Canton, Ohio', 'Steubenville, Ohio', 'Youngstown, Ohio', 'Austin, Texas']

# ['Hayward, California', 'Huntington Beach, California', 'Lafayette, California', 'Los Angeles, California', 'Manhattan Beach, California', 'Palm Springs, California', 'Pasadena, California', 'Sausalito, California', 'Arvada, Colorado', 'Englewood, Colorado', 'Golden, Colorado', 'La Junta, Colorado', 'Las Animas, Colorado', 'Westminster, Colorado', 'Wheat Ridge, Colorado', 'Brookfield, Connecticut', 'Westport, Connecticut', 'Bartow, Florida', 'Palm Beach, Florida', 'Buford, Georgia', 'Vienna, Georgia', 'Carbondale, Illinois', 'Savanna, Illinois', 'Spencer, Indiana', 'Dodge City, Kansas', 'Emporia, Kansas', 'Garden City, Kansas', 'Great Bend, Kansas', 'Hays, Kansas', 'Junction City, Kansas', 'Kansas City, Kansas', 'Leavenworth, Kansas', 'Leawood, Kansas', 'Overland Park, Kansas', 'Pittsburg, Kansas', 'Prairie Village, Kansas', 'Salina, Kansas', 'Shawnee, Kansas', 'New Iberia, Louisiana', 'Nantucket, Massachusetts', 'Park Rapids, Minnesota', 'Columbia, Missouri', 'Bayonne, New Jersey', 'Woodstock, New York', 'Minot, North Dakota', 'Kent, Ohio', 'Henryetta, Oklahoma', 'Cave Junction, Oregon', 'Hillsboro, Oregon', 'Sheridan, Oregon', 'Allentown, Pennsylvania', 'Harrisburg, Pennsylvania', 'Lock Haven, Pennsylvania', 'Annandale, Virginia', 'Arlington, Virginia', 'Great Falls, Virginia', 'Everett, Washington']
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ['Lowell, Massachusetts', 'Saugus, Massachusetts', 'Bloomfield Hills, Michigan', 'Sedalia, Missouri', 'Lincoln, Nebraska', 'Las Vegas, Nevada', 'Trenton, New Jersey', 'Albuquerque, New Mexico', 'New Rochelle, New York', 'Rochester, New York', 'Fargo, North Dakota', 'Canton, Ohio', 'Steubenville, Ohio', 'Youngstown, Ohio', 'Erie, Pennsylvania', 'York, Pennsylvania', 'Austin, Texas']

