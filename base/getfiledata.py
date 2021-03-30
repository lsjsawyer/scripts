import os

import yaml


class GetFileData:

    def __init__(self):
        ...

    def get_yaml_data(self, name):
        file_path = os.getcwd() + os.sep + "data" + os.sep + name
        with open(file_path, "r", encoding="utf-8")as f:
            return yaml.safe_load(f)
            # data = yaml.safe_load(f)
            # print(data)