

import yaml
class YamlHandler(object):
    def __init__(self, file):
        self.file = file
    def read_yaml(self, encoding='utf-8'):
        with open(self.file, 'r', encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    def write_yaml(self, data, encoding='utf-8'):
        with open(self.file, 'w', encoding=encoding) as f:
            f.write(yaml.dump(data))