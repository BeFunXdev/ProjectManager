import json
import os

from src.config.jsonFiles import DataFiles


class ConfigReader:

    @staticmethod
    def _get_path(name):
        return f"./ProjectManager/{name}.json"

    @staticmethod
    def read_command():
        data = []

        with open(f'./ProjectManager/{DataFiles.COMMANDS}.json') as fn:
            json.load(fn)

        return data

    @staticmethod
    def json_read(file_name):
        if os.path.isfile(ConfigReader._get_path(file_name)):
            with open(ConfigReader._get_path(file_name), "r") as fh:
                return json.load(fh)
        else:
            return []

    @staticmethod
    def json_write(file_name, data):
        with open(ConfigReader._get_path(file_name), "w") as fh:
            json.dump(data, fh)
