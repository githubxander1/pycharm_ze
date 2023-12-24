from pprint import pprint

import yaml


def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
# pprint(load_yaml(f'../data/user.yaml'))