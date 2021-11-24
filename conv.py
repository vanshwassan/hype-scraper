import json
import csv

with open('data.json') as f:
    data = json.load(f)


def getUsernames():
    i = 0
    list = []
    while (i < 200):
        a = data['users'][i]['screen_name']
        list.append(a)
        i = i + 1
    return list


list = getUsernames()

print(list)

with open('web3_org.csv', 'w') as file:
    wr = csv.writer(file)
    wr.writerow(list)
