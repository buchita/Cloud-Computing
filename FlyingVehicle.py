# Program: Flying Vehicle in ascending order in the web api called www.swapi.io.
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


def next_info(something):
    info = something.json()['results']
    return info

# find the cargo capacity and store in a list
def cargo_cap(info, cargo_amount):
    for v in info:
        # if the element is not equal to land vehicles
        if v['vehicle_class'] != 'wheeled' and v['vehicle_class'] != 'wheeled walker' and v['vehicle_class'] != 'walker' and v['vehicle_class'] != 'droid tank' and v['vehicle_class'] != 'assault walker' and v['vehicle_class'] != 'submarine':
            # if equals to 'none' or 'unknown'
            if v['cargo_capacity'] == 'none' or v['cargo_capacity'] == 'unknown':
                pass
            else:
                cap = int(v['cargo_capacity'])
                cargo_amount.append(cap)
    return cargo_amount

# -----------------------------------------------
req = requests.get('https://swapi.co/api/vehicles')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# list for storing the cargo capacity from each vehicle
cargo_amount = []

# while its not the last page
while url != prev:
    # get the cargo capacity from each page
    cargo_amount = cargo_cap(info, cargo_amount)

    # get the req num
    req = getinfo(url)

    # get the next url
    url = the_URL(req)

    # get the info of the page
    info = next_info(req)

# get the cargo capacity for the last page
cargo_amount = cargo_cap(info, cargo_amount)

# sort the list in ascending order using sort()
cargo_amount.sort()

print("The ascending order of cargo capacity: ")
print(cargo_amount)