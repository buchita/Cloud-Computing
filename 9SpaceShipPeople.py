# For all people associated with spaceships, list their names,
# the spaceships’ names and the cost of each spaceship
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

# empty dicts
dict_people_spaceship = {}
em_lis = []

# while not the last page
while url != prev:
    # reads in the dictionary
    for p in info:
        # ignore all the ones that do not have anything to do with the spaceship
        if p['starships'] == em_lis:
            pass

        else:
            dict_people_spaceship[p['name']] = p['starships']

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)
# for last page
for p in info:
    # ignore the empty ones
    if p['starships'] == em_lis:
        pass

    else:
        dict_people_spaceship[p['name']] = p['starships']

# loops through the dict
for k, v in dict_people_spaceship.items():
    print("-------------")

    print("{}{}".format("Person: ", k,))

    # looping through the list of links ie value
    for i, link in enumerate(v):
        # get the url and looks into name and price for the spaceship
        re = requests.get(link)
        name_space = re.json()['name']
        price = re.json()['cost_in_credits']

        print("{}{}{}{}".format("Spaceship: ", name_space, " Price: ", price))
