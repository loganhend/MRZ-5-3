import json


def upload_weights(columns, weights1, weights2):
    with open('w0.json', 'w', encoding="utf-8") as file:
        dictionary = {"col": columns, "w1": weights1, "w2": weights2}
        json.dump(dictionary, file, indent=2)


def download_weights():
    with open('w0.json', 'r', encoding="utf-8") as conf:
        information = json.load(conf)
        return information['col'], information['w1'], information['w2']


def download_sequences():
    with open('s_conf.json', 'r', encoding="utf-8") as seq:
        information = json.load(seq)
        return information['sequences']
