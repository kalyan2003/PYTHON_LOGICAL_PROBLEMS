import json

json_file = open("JSON_file.json","r")
data = json.load(json_file)

if "name" in data:
    data["name"] = "Kalyan"
else:
    print("key is not existing")


json_file = open("JSON_file.json","w")

json.dump(data,json_file)


