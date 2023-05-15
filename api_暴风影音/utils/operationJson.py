#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:张红
import os.path

# from common.public import base_dir
import json
import yaml

from api_暴风影音.common.public import base_dir


def readJson():
         return json.load(open(file=os.path.join(base_dir(),'data','fengbao.json'),encoding='utf-8'))

# print(readJson())

def readYaml():
        with open(file=os.path.join(base_dir(),'config','url.yaml'),encoding="utf-8")as f:
            return yaml.safe_load(f)
# print(readYaml())