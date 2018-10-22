# find the name and planet origin of the species is associated with the largest number of characters (people)?
# By: Buchita Gitchamnan
# 18/10/2018
# Interpreter: PyCharm

import requests

# get the request num from the url
def getinfo(linko):
    req = requests.get(linko)
    print(req)
    return req


# reading and getting the url from the page to the next page
def the_URL(next_page):
    page =next_page.json()['next']
    print(page)
    return page


# get the information of the result section
def next_info(something):
    info = something.json()['results']
    return info


# ------------------------------------------
req = requests.get('https://swapi.co/api/species/')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# empty dictionaries
dict_people = {}
dict_species = {}

# while not the last page
while url != prev:
    # reads in the values for dicts
    for p in info:
        dict_people[p['name']] = len(p['people'])   # name of the species and amount of characters associated
        dict_species[p['name']] = p['homeworld']    # name of peeps with the link of home world

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)

# last page
for p in info:
    dict_people[p['name']] = len(p['people'])
    dict_species[p['name']] = p['homeworld']

# sorts in ascending order using the value
sort_people_tuple = sorted(dict_people.items(), key=lambda value: value[1])

# converts into a dictionary
sort_people_dict = dict(sort_people_tuple)

# get the key and value of the highest value
key_highest, value_highest = max(sort_people_dict.items(), key=lambda x: x[1])

# loops in the dict
for k, v in dict_species.items():
    # check for the same name of the species in the 2 dicts
    if k == key_highest:
        # get the url and looks into the name of the planet
        req1 = requests.get(v)
        planet_name = req1.json()['name']  # get the detail of the page

print("{}{}".format("The name of the species with the most associated chars is ", key_highest))
print("{}{}".format("The planet origin is ", planet_name))
