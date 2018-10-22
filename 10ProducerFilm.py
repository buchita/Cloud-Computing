# find the producer’s name who has been involved the
# greatest number of films?
# By: Buchita Gitchamnan
# 18/10/2018
# Interpreter: PyCharm


import requests

# connect to the api
req = requests.get('https://swapi.co/api/films/')
url = req.json()['next']   # get the next url
prev = req.json()['previous']   # get the value of the last page
info = req.json()['results']    # get the detail of the page

# variables
em_lis = []
pro_lis = []
temp_pro = []
count = 0
final_dict = {}

# has only 1 page of films
for f in info:
    # gets the name of producers in a movie
    tem_str = f['producer']

    # splits the names using ,
    # add the names in pro_lis
    pro_lis.append(tem_str.split(","))

# goes through the list of list of names
for i in pro_lis:
    # converting to a single list
    for j in i:
        temp_pro.append(j)

# goes through the list
for x in range(0, len(temp_pro)):
    # remove the start string whitespace - strip leading space.
    temp_pro[x] = temp_pro[x].lstrip()

    # count the repeating name
    count1 = temp_pro.count(temp_pro[x])

    # add in a dict
    final_dict[temp_pro[x]] = count1

    # get the highest count num
    if count1 > count:
        count = count1

# sorts the dict in ascending order using the value
sort_tuple = sorted(final_dict.items(), key=lambda value: value[1])

# converts the tuple to dictionary
new_sort_dict_producer = dict(sort_tuple)

# get the highest value out of the values in the dict
key, value = max(new_sort_dict_producer.items(), key=lambda y: y[1])

print("{}{}".format("The producer who has been involved the greatest number of films is ", key))
