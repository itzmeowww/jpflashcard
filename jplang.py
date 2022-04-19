import requests
from bs4 import BeautifulSoup
import json
import romkan


def generate(idx):
    pages = []
    filename = f'{idx}_jplang'

    base_url = f'https://jplang.tufs.ac.jp/en/nw/{idx}/{idx}.html'

    pages.append(base_url)

    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    words = []

    for page in pages:
        print(f'fetching  {page} ...')
        res = requests.get(page)
        soup = BeautifulSoup(res.content, 'html.parser')
        ul = soup.find(id='new_word')
        for li in ul.find_all('li'):
            word = li.find(class_='word')
            kanji = li.find(class_='kanji')
            translation = li.find(class_='translation')

            if not kanji:
                kanji = ''
            else:
                kanji = kanji.get_text()
            if word and translation:
                word = word.get_text()
                translation = translation.get_text()
            words.append(
                {
                    "word": word,
                    "kanji": kanji,
                    "translation": translation
                }
            )
            # print(word, kanji, translation)

        print(f'fetching {page} ... completed')

    json_string = json.dumps(words)
    path = f'web/src/data/{filename}.json'
    with open(path, 'w') as outfile:
        outfile.write(json_string)
        print(f'{len(words)} words are saved in {path} ')


for i in range(28):
    generate(i+1)
