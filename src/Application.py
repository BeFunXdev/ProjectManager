import os.path
import sys
from typing import List

from src.commandParser.CommandParser import CommandParser
from src.config.jsonFiles import DataFiles
from src.configReader.ConfigReader import ConfigReader
from src.dataClass.Parser import SubParser, Param


class Application:
    def __init__(self):
        self.command_parser = CommandParser()
        self.reader = ConfigReader()

    def parse(self, args):

        self.command_parser.add_command(
            SubParser(name="add", help="Добавляет новый проект"),
            [Param(name='name', help='Задайте алиас для своего проекта'), Param(name='path', help='Путь до вашего проекта')],
            self._add
        )

        self.command_parser.add_command(
            SubParser(name="start", help="Добавляет новый проект"),
            [Param(name='name', help='Задайте алиас для своего проекта')],
            self._start
        )

        print('command add')
        print(DataFiles.PROJECT_LIST)

        if len(args) == 0:
            self.command_parser.help()
            sys.exit(1)
        else:
            self.command_parser.execute(args)
        # args = self.parser.parse_args(args)
        # args.func(args)

    def _add(self, args):
        data = self.reader.json_read(DataFiles.PROJECT_LIST)

        if args.name in data:
            print("Такой проект уже существует")
            exit(0)
        else:
            data.append({"name": args.name, "path": os.path.abspath(args.path)})
            self.reader.json_write(DataFiles.PROJECT_LIST, data)

    def _start(self, args):
        project = Application._find_project(self.reader.json_read(DataFiles.PROJECT_LIST), args.name)

        if (project == None):
            print('Такого проекта нет!')
            exit(0)

        os.system('startdb')
        os.system(f"wt -w 0 nt -d {project['path'] + '/frontend'} powershell yarn dev")
        os.system(f"wt -w 0 nt -d {project['path'] + '/backend'} powershell yarn start:dev")

    @staticmethod
    def _find_project(array, value):
        for item in array:
            if item["name"] == value:
                return item
