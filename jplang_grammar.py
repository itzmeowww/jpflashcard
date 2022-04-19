from email.mime import base
from lib2to3.pgen2 import grammar
import requests
from bs4 import BeautifulSoup
import json
import romkan
words = {}


def generate(idx):
    chapter = idx
    pages = []
    # filename = f'{idx}_jplag'
    base_url = ''
    if idx in [1, 4, 6, 7, 8, 13, 14, 15, 16, 27, 28]:
        base_url = f'https://jplang.tufs.ac.jp/en/bu/{idx}/{idx}-1-1.html'
    else:
        base_url = f'https://jplang.tufs.ac.jp/en/bu/{idx}/{idx}-1.html'

    print(base)
    pages.append(base_url)

    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    # words = []

    for page in pages:
        print(f'fetching {page} ...')
        res = requests.get(page)
        soup = BeautifulSoup(res.content, 'html.parser')
        dd = soup.find('dd', class_='open')
        # print(dd)
        ul = dd.find('ul')
        for li in ul.find_all('li'):
            grammar = li.find('a')
            if grammar:
                if chapter not in words:
                    words[chapter] = []
                words[chapter].append(grammar.get_text())
                # print(grammar.get_text())

        print(f'fetching {page} ... completed')


for i in range(28):
    generate(i+1)

json_string = json.dumps(words)
path = f'web/src/data/jplang_grammar.json'
with open(path, 'w') as outfile:
    outfile.write(json_string)
    print(f'{len(words)} words are saved in {path} ')
