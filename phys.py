
import json

# Opening JSON file
f = open('physics.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for x in data:
    for i in data[x]:
        print(f"{i['kanji']}    {i['hiragana']}    {i['meaning']}")

# Closing file
f.close()
