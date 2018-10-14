# Program: To count how many people are in the web api called www.swapi.io without using the given counter.
# By: Buchita Gitchamnan
# 11/10/2018
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
    return page


# counting how many names in your bois page
def counting(info, x):
    # for an element in the info which is the long paragraph in the 'results'
    for p in info:
        # find 'name'
        if p['name']:
            # increment the count
            x = x + 1
    print(x)
    return x

# -----------------1
# get info from the page
req = requests.get('https://swapi.co/api/people')

# the url for the next page
data = req.json()['next']

# store the word of the last page
prev = req.json()['previous']

# getting the info about names, heights etc...
info = req.json()['results']

# count for peeps
count = 0

# passing to count name on each page
count = counting(info, count)

# ---------- 2
# getting the req num
req_num = getinfo(data)

# get the next url
next_url = the_URL(req_num)

# -------the rest til 8
while next_url != prev:
    print("The url " + next_url)

    # fetch the info
    information = req_num.json()['results']

    print(information)

    # pass the info to count for people
    count = counting(information, count)

    # get another request num for the next url
    req_num = getinfo(next_url)

    # get the url from that page
    next_url = the_URL(req_num)

# --------last page
information = req_num.json()['results']
print(information)
count = counting(information, count)

print("The Total count: ")
print(count)