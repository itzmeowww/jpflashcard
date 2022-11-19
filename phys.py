
import json

# Opening JSON file
f = open('physics2.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
used = []
with open('physic2.txt', 'w') as f:
    for x in data:
        for i in data[x]:
            if i['kanji'] in used:
                continue
            used.append(i['kanji'])
            print(i)
            f.write(f"{i['kanji']}    {i['hiragana']}    {i['meaning']}\n")

# Closing file
f.close()
