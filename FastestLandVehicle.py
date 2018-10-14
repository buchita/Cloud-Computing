# Program: Land vehicle in the web api called www.swapi.io.
# By: Buchita Gitchamnan
# 11/10/2018
# Interpreter: PyCharm


import requests

name = ''

# get the request num from the url
def getinfo(linko):
    req = requests.get(linko)
    print(req)
    return req


# reading and getting the url from the page to the next page
def the_URL(next_page):
    page =next_page.json()['next']
    return page


def next_info(something):
    info = something.json()['results']
    return info


def high_value(info, max_value):

    try:
        # for every element in info
        for v in info:
            # fliter the land vehicles
            if v['vehicle_class'] == 'wheeled' or v['vehicle_class'] == 'wheeled walker' or v['vehicle_class'] == 'walker' or v['vehicle_class'] == 'droid tank' or v['vehicle_class'] == 'assault walker':

                # catch for ' unknown ' value
                if v['max_atmosphering_speed'] == 'unknown':

                    # ignore this
                    pass
                # comparing the values
                if int(v['max_atmosphering_speed']) > int(max_value):

                    # assign the highest value
                    max_value = v['max_atmosphering_speed']

                    # declare a global variable for saving the name of highest speed
                    global name
                    name = v['name']

    except ValueError:
        pass

    print(max_value)
    return max_value


# --------------------------------
req = requests.get('https://swapi.co/api/vehicles')     # get request number
data = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# for storing the max value
max_value = 0

# while its not the last page
while data != prev:
    # calculating the highest value
    max_value = high_value(info, max_value)

    # getting the request num
    req_num = getinfo(data)

    # get the next url
    data = the_URL(req_num)
    print(data)

    # get the content of the page
    info = next_info(req_num)
    print(info)

# getting the highest value of the last page
max_value = high_value(info, max_value)

# print value and name out
print('The highest value: ' + max_value)
print('The name of highest: ' + name)