import requests
from bs4 import BeautifulSoup
import json
import romkan


def generate(idx):
    pages = []
    filename = f'n{idx}_vocab'

    base_url = f'https://jlptsensei.com/jlpt-n{idx}-vocabulary-list/'

    pages.append(base_url)

    res = requests.get(base_url)
    soup = BeautifulSoup(res.content, 'html.parser')

    for pagination in soup.find_all(class_='page-numbers'):
        if len(pagination['class']) == 1:
            pages.append(pagination['href'])

    words = []

    for page in pages:
        print(f'fetching  {page} ...')
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
                v_type = v_type_div.string.strip()
                v_type = ','.join(v_type.split(','))

                isKatakana = False

                if 'Katakana' in v_type:
                    isKatakana = True
                    v_type = v_type.replace('Katakana', '').strip()

                v_div_a = v_div.find('a')
                v = v_div_a.string.strip()
                href = v_div_a['href'],

                vr_div_a = vr_div.find('a')
                p = vr_div_a.find('p')
                p.decompose()

                hiragana = ''
                if not isKatakana:
                    hiragana = romkan.to_hiragana(vr_div_a.string)
                vr = vr_div_a.string.strip(),

                vm = vm_div.string
                words.append({
                    'num': num,
                    'word': v,
                    'reading': vr,
                    'reading_hiragana': hiragana,
                    'type': v_type,
                    'meaning': vm,
                    'href': href,
                    'isKatakana': isKatakana,
                })
            # print(num)
            # print(v_list)
            # print(vr_list)
            # print(v_type)
            # print(vm)
        # print()
        print(f'fetching {page} ... completed')

    json_string = json.dumps(words)
    path = f'web/src/data/{filename}.json'
    with open(path, 'w') as outfile:
        outfile.write(json_string)
        print(f'{len(words)} words are saved in {path} ')


for i in range(5):
    generate(i+1)
