
import os
import json

if (os.name == 'nt'):
    path = os.path.dirname(__file__) +'\\testdata.json'
elif (os.name == 'posix'):
    path = os.path.dirname(__file__) +'/testdata.json'
else:
    path = os.path.dirname(__file__) +'/testdata.json'


with open(path,encoding="UTF-8") as json_file:
    data = json.load(json_file)
    for p in data['data']:
        availability=p["availability"]
        dish=p["dish"]
        description=p["descriptions"]


