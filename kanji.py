import requests
from bs4 import BeautifulSoup
import json
import romkan


pages = []

filename = 'n1_kanji'
# base_url = 'https://jlptsensei.com/jlpt-n5-nouns-vocabulary-list/'
# base_url = 'https://jlptsensei.com/jlpt-n5-vocabulary-list/'
base_url = 'https://jlptsensei.com/jlpt-n1-kanji-list/'

pages.append(base_url)

res = requests.get(base_url)
soup = BeautifulSoup(res.content, 'html.parser')

for pagination in soup.find_all(class_='page-numbers'):
    if len(pagination['class']) == 1:
        pages.append(pagination['href'])

words = []

for page in pages:
    print(f'fecting ${page} ...')
    res = requests.get(page)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.find('table')
    for row in table.find_all('tr'):

        # debug
        # for col in row.find_all('td'):
        #     print(col)

        num_div = row.find(class_='jl-td-num')
        k_div = row.find(class_='jl-td-k')
        on_div = row.find(class_='jl-td-on')
        kun_div = row.find(class_='jl-td-kun')
        m_div = row.find(class_='jl-td-m')

        if num_div and k_div and on_div and kun_div and m_div:
            num = num_div.string
            # print(num)
            k_div_a = k_div.find('a')
            k = {
                'string': k_div_a.string.strip(),
                'href':  k_div_a['href'],
            }

            on = []
            on_div_a = on_div.find('a')
            p = on_div_a.find('p')
            if p.string:
                on.append({
                    'string': p.string.strip(),
                })
            else:
                on.append({
                    'string': '',
                })
            p.decompose()
            if on_div_a.string:
                on.append({
                    'string': on_div_a.string.strip(),

                })
            else:
                on.append({
                    'string': '',

                })
            kun = []
            kun_div_a = kun_div.find('a')

            p = kun_div_a.find('p')
            if p.string:
                kun.append({
                    'string': p.string.strip(),
                })
            else:
                kun.append({
                    'string': '',
                })

            p.decompose()
            if kun_div_a.string:
                kun.append({
                    'string': kun_div_a.string.strip(),
                })
            else:
                kun.append({
                    'string': '',
                })
            m = m_div.string.strip()
            words.append({
                'num': num,
                'k': k,
                'on': on,
                'kun': kun,
                'm': m
            })
        # print(num)
        # print(v_list)
        # print(vr_list)
        # print(v_type)
        # print(vm)
    # print()
    print(f'fecting ${page} ... completed')


json_string = json.dumps(words)
path = f'web/src/data/{filename}.json'
with open(path, 'w') as outfile:
    outfile.write(json_string)
    print(f'{len(words)} words are saved in {path} ')
