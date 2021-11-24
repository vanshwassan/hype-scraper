import requests
import csv
import config
import json


def getUsers():
    PARAMS = {'list_id': '1460714501368532992', 'count': '500'}
    URL = "https://api.twitter.com/1.1/lists/members.json"

    r = requests.get(url=URL, params=PARAMS, headers=config.HEADERS)
    data = r.json()
    with open('data.json', 'w') as f:
        json.dump(data, f)


print(getUsers())
