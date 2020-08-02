import json

with open("C:\\Users\\raysp\\Desktop\\Python\\Personal\\BirbBot\\resources\\testJson.json") as jsonFile:
    data = json.load(jsonFile)
    for i in data["Chivalry servers"]:
        print(i["Name"])