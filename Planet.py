# List the names of all planets sorted by (one list each)
#           1. diameter in ascending order
#           2. population in descending order
# By: Buchita Gitchamnan
# 13/10/2018
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


# add the details in a dict for diameter
def diameter(info, dia_dict):
    for p in info:
        # add the 'unknown value in a separate dictionary
        if p['diameter'] == 'unknown':
            # make it global so can access it from anywhere, 2 return types will be tuple and will make things complex
            global temp_dia_dict
            temp_dia_dict[p['name']] = 'unknown'
        else:
            # make a dict with all the names and diameters
            dia_dict[p['name']] = int(p['diameter'])

    return dia_dict


# add the details in a dict for population
def population(info, pop_dict):
    for p in info:
        # add the 'unknown value in a separate dictionary
        if p['population'] == 'unknown':
            # make it global so can access it from anywhere, 2 return types will be tuple and will make things complex
            global temp_pop_dict
            temp_pop_dict[p['name']] = 'unknown'
        else:
            pop_dict[p['name']] = int(p['population'])
    return pop_dict


# ---------------------------------------

req = requests.get('https://swapi.co/api/planets/')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# create dictionaries
dia_dict = {}
temp_dia_dict = {}
pop_dict = {}
temp_pop_dict = {}

# while its not the last page
while url != prev:
    # pass to make dicts
    dia_dict = diameter(info, dia_dict)
    pop_dict = population(info, pop_dict)

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)

# pass to make dicts for the last page
dia_dict = diameter(info, dia_dict)
pop_dict = population(info, pop_dict)

# sort_dia is a list of tuples sorted by the second element in each tuple
sort_dia = sorted(dia_dict.items(), key=lambda value: value[1])

# convert tuple to dict
new_dia = dict(sort_dia)

# stick back the planets with 'unknown' to the dia dict
for key, value in temp_dia_dict.items():
    new_dia[key] = value

# sort dict in a descending order looking at its values this returns a list of tuples
sort_pop = sorted(pop_dict.items(), key=lambda value: value[1], reverse=True)

# convert a tuple to dict
new_pop = dict(sort_pop)

# read back in the dict for ' unknown' value pop dict.
for key, value in temp_pop_dict.items():
    new_pop[key] = value

# print dicts with the values of the planets
print("{} {}".format("The List of names of all the planets sorted by diameter in ascending order:", new_dia))
print("{} {}".format("The List of names of all the planets sorted by population in descending order:", new_pop))

