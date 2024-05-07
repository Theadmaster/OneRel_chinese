import json
import os
def save_data():
    data_folder = os.path.join('..', 'data', 'ca')
    json_in_file = 'test.json'
    json_out_file = os.path.join('test_triples.json')
    res = []
    with open(json_in_file, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line.strip())
            text = data['text']
            rels = data['spo_list']
            new_rels = []
            for rel in rels:
                pred = rel['predicate']
                sub = rel['subject']
                obj = rel['object']
                item = [sub, pred, obj]
                new_rels.append(item)
            res.append({'text': text, 'triple_list': new_rels})

    with open(os.path.join(data_folder, json_out_file), 'w', encoding='utf-8') as file:
        for item in res:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

if __name__ == '__main__':
    save_data()