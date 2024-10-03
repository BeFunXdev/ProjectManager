import argparse
import os.path
import sys
import json


class Application:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="CLI-приложение на Python с подкомандами")
        self.subparsers = self.parser.add_subparsers()

    def parse(self, args):
        parser_add = self.subparsers.add_parser("add", help="Добовляет проект")
        parser_add.add_argument("name", help="Введите название проекта")
        parser_add.add_argument("path", help="Введите название проекта")
        parser_add.set_defaults(func=self._add)

        parser_start = self.subparsers.add_parser("start", help="Добовляет проект")
        parser_start.add_argument("name", help="Введите название проекта")
        parser_start.set_defaults(func=self._start)

        if len(args) == 0:
            self.parser.print_help()
            sys.exit(1)
        # elif len(args) == 1:
        #     self._start(args[0])

        args = self.parser.parse_args(args)
        args.func(args)

    def _add(self, args):

        data = self._json_read()

        if args.name in data:
            print("Такой проект уже существует")
            exit(0)
        else:
            data.append({"name": args.name, "path": os.path.abspath(args.path)})
            self._json_write(data)

    def _start(self, args):
        project = self._find_project(self._json_read(), args.name)

        os.system(f"wt -w 0 nt -d {project['path'] + '/frontend'} powershell yarn dev")


    def _json_read(self):
        if os.path.isfile('./ProjectManager/projectList.json'):
            with open("./ProjectManager/projectList.json", "r") as fh:
                return json.load(fh)
        else:
            return []

    def _json_write(self, data):
        with open("./ProjectManager/projectList.json", "w") as fh:
            json.dump(data, fh)

    def _find_project(self, array, value):
        for item in array:
            if item["name"] == value:
                return item