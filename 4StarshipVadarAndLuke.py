# Find how many distinct star ships are associated with Darth Vadar and Luke Skywalker
# By: Buchita Gitchamnan
# 13/10/2018
# Interpreter: PyCharm

import requests


# -----------------------------------------------
# Luke
req1 = requests.get('https://swapi.co/api/people/1/')
name_luke = req1.json()['name']   # get the name
starships_luke = req1.json()['starships']    # get the list of star ship urls

# Darth Vadar
req2 = requests.get('https://swapi.co/api/people/4/')
name_vadar = req2.json()['name']   # get the name
starships_vadar = req2.json()['starships']    # get the list of star ship urls

length_star_luke = len(starships_luke)
length_star_vadar = len(starships_vadar)

print("{}{}".format("Name: ", name_luke))
print("{}{}".format("Distinct starships: ", length_star_luke))

print("-----------------")

print("{}{}".format("Name: ", name_vadar))
print("{}{}".format("Distinct starships: ", length_star_vadar))
