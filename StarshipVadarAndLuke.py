# Find how many distinct star ships are associated with Darth Vadar and Luke Skywalker
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

def flim_info(something):
    info = something.json()['characters']
    return info


# -----------------------------------------------

req = requests.get('https://swapi.co/api/starships')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

movie_url = []
name_starships = []
i = 0

for s in info:
    # storing the movie urls from each starship page one by one
    movie_url = s['films']
    print(len(movie_url))
    # iterate through each url
    while i <= len(movie_url):
        # counter for the urls
        print(i)
        i = i+1

        f_req = getinfo(movie_url[i])
        print(f_req)

        m_info = flim_info(f_req)

        for p in m_info:
            if p == 'https://swapi.co/api/people/1/' or p == 'https://swapi.co/api/people/4/':
                name_starships = s['name']
                print(name_starships)