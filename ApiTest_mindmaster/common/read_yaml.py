from pprint import pprint

import yaml


def readYaml():
    with open('../data/loginDataParameter.yaml', 'r',encoding='utf-8') as f:
        yamldata =yaml.load(f,Loader=yaml.Loader)
        return yamldata
        # return list(yamldata)

pprint(readYaml())