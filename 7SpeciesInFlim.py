# Program: Find which species appears second most often in a film
# By: Buchita Gitchamnan
# 16/10/2018
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

def convertDict(info, dict_film):
    for sp in info:
        dict_film[sp['name']] = len(sp['films'])
    return dict_film

# ---------------------------------------

req = requests.get('https://swapi.co/api/species/')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# empty dict
dict_film = {}

# while its not the last page
while url != prev:
    # read the name and the film in the dict
    dict_film = convertDict(info, dict_film)

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)


# read the name and the film in the dict
dict_film = convertDict(info, dict_film)

sort_dict = sorted(dict_film.items(), key=lambda value: value[1], reverse=True)
new_dict_film = dict(sort_dict)

em_li = []

# -----------the first value
key, value = max(new_dict_film.items(), key=lambda x:x[1])

del new_dict_film[key]

count = 0

# make a copy where the size of the dict is still the same when deleting the element in the loop
# avoid the run time error
for k, v in new_dict_film.copy().items():
    while count < 2:

        key1, value1 = max(new_dict_film.items(), key=lambda x: x[1])

        value = value1

        value1 = v

        # delete the key and value
        del new_dict_film[key1]

        count = count + 1

        # get the max value
        key2, value2 = max(new_dict_film.items(), key=lambda x: x[1])

        em_li = key2

        print("{} {}".format("The second most species appeared in a film:", key2))

