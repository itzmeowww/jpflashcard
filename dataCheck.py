import json

with open('./web/src/data/n5_vocab.json') as f:
    data = json.load(f)

for word in data:

    if len(word['v']) != 1:
        print(len(word['v']))
