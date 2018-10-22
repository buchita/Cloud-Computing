# Program: To count how many people are in the web api called www.swapi.io without using the given counter.
# By: Buchita Gitchamnan
# 11/10/2018
# Interpreter: PyCharm


import requests


# get the request num from the url
def getinfo(linko):
    req1 = requests.get(linko)
    print(req1)
    return req1


# reading and getting the url from the page to the next page
def the_URL(next_page):
    page =next_page.json()['next']
    print(page)
    return page

# get the information of the result section
def next_info(something):
    info = something.json()['results']
    return info


# counting how many names in your bois page
def counting(info, x):
    # for an element in the info which is the long paragraph in the 'results'
    for p in info:
        # find 'name'
        if p['name']:
            # increment the count
            x = x + 1
    return x


# -----------------1
# get info from the page
req = requests.get('https://swapi.co/api/people')
url = req.json()['next']   # the url for the next page
prev = req.json()['previous']   # store the word of the last page
info = req.json()['results']    # getting the info about names, heights etc...

# count for peeps
count = 0

# while its not the last page
while url != prev:
    # passing to count name on each page
    count = counting(info, count)

    # get the next req num, url and details of the results
    req = getinfo(url)
    url = the_URL(req)
    info = next_info(req)


# --------last page
information = req.json()['results']
count = counting(information, count)

print("{}{}".format("The Total count: ", count))
