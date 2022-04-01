import requests
from bs4 import BeautifulSoup
import json
import romkan


pages = []

filename = 'n1_vocab'
# base_url = 'https://jlptsensei.com/jlpt-n5-nouns-vocabulary-list/'
# base_url = 'https://jlptsensei.com/jlpt-n5-vocabulary-list/'
base_url = 'https://jlptsensei.com/jlpt-n1-vocabulary-list/'

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
        v_div = row.find(class_='jl-td-v')

        vr_div = row.find(class_='jl-td-vr')
        v_type_div = row.find(class_='jl-td-v-type')
        vm_div = row.find(class_='jl-td-vm')

        # print(num_div, v_div, vr_div, v_type_div, vm_div)
        if num_div and v_div and vr_div and v_type_div and vm_div:
            num = num_div.string
            v_type = v_type_div.string
            v_type = ','.join(v_type.split(','))

            isKatakana = False

            if 'Katakana' in v_type:
                isKatakana = True
                v_type = v_type.replace('Katakana', '').strip()

            v_list = []
            for v_div_a in v_div.find_all('a'):

                v_list.append({
                    'string': v_div_a.string.strip(),
                    'href':  v_div_a['href'],

                })

            vr_list = []
            for vr_div_a in vr_div.find_all('a'):
                p = vr_div_a.find('p')
                p.decompose()

                hiragana = ''
                if not isKatakana:
                    hiragana = romkan.to_hiragana(vr_div_a.string)
                vr_list.append({
                    'string': vr_div_a.string.strip(),
                    'href':  vr_div_a['href'],
                    'hiragana': hiragana
                })

            vm = vm_div.string
            words.append({
                'num': num,
                'v': v_list,
                'vr': vr_list,
                'vType': v_type,
                'vm': vm,
                'isKatakana': isKatakana,
                "hiragana": hiragana
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
