# find character has the most associated films?
# When was the first and last of their films released?
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
req = requests.get('https://swapi.co/api/people/')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# declare empty dicts
dict_film = {}
dict_count = {}

# while there's a next page
while url != prev:
    # reading in the dicts
    for c in info:
        dict_film[c['name']] = c['films']   # reads in names and a list of movies
        dict_count[c['name']] = len(c['films'])  # reads in names and amount of movies

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)

# for the page
for c in info:
    dict_film[c['name']] = c['films']
    dict_count[c['name']] = len(c['films'])

# sorts the dict in ascending order using the value
sort_tuple = sorted(dict_count.items(), key=lambda value: value[1])

# converts the tuple to dictionary
new_sort_dict_count = dict(sort_tuple)

# get the highest value out of the values in the dict
key, value = max(new_sort_dict_count.items(), key=lambda x: x[1])

# loops through all the elements
for k,v in dict_film.items():

    # checks if the element is equals to the name of the character with the highest value of the movies
    if k == key:
        # get the tile of the first movie
        req = requests.get(v[0])
        title_first = req.json()['title']

        # get the title of the last
        req = requests.get(v[-1])
        title_last = req.json()['title']

        print("{} {}".format("The character who has associated with most movie is", key))
        print("{} {}".format("The first movie is:", title_first))
        print("{} {}".format("The last movie is:", title_last))

