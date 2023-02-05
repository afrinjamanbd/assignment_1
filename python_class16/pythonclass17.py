import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

for i in data:
    print(i)
  
# Closing file
f.close()


appDict = {
  'name': 'messenger',
  'playstore': True,
  'company': 'Facebook',
  'price': 100
}
app_json = json.dumps(appDict)
print(app_json)


# data[0]['title']