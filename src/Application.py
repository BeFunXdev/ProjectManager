import sys

from src.commandParser.CommandParser import CommandParser
from src.config.jsonFiles import DataFiles
from src.configReader.ConfigReader import ConfigReader
from src.dataClass.Parser import SubParser, Param
from src.strategy.StrategyMenager import StrategyManager


class Application:
    def __init__(self):
        self.command_parser = CommandParser()
        self.reader = ConfigReader()
        self.strategyManager = StrategyManager()

    def parse(self, args):

        self.command_parser.add_command(
            SubParser(name="add", help="Добавляет новый проект"),
            [Param(name='name', help='Задайте алиас для своего проекта'),
             Param(name='path', help='Путь до вашего проекта'),
             Param(name='-t', help='Тип проекта(бета)')],
            self._add
        )

        self.command_parser.add_command(
            SubParser(name="start", help="Добавляет новый проект"),
            [Param(name='name', help='Задайте алиас для своего проекта')],
            self._start
        )

        self.command_parser.add_command(
            SubParser(name="delete", help="Удоляет проект"),
            [Param(name='name', help='Введите алиас своего проекта')],
            self._delete
        )

        self.command_parser.add_command(
            SubParser(name="list", help="Ввыводит все проекты"),
            [],
            self._list
        )

        if len(args) == 0:
            self.command_parser.help()
            sys.exit(1)
        else:
            self.command_parser.execute(args)
            exit(0)

    def _add(self, args):
        strategy = self.strategyManager.get_strategy(args.t)
        data = self.reader.json_read(DataFiles.PROJECT_LIST)

        if args.name in data:
            print("Такой проект уже существует")
            exit(0)
        else:
            data = strategy.add(data, args)
            self.reader.json_write(DataFiles.PROJECT_LIST, data)
        exit(0)

    def _delete(self, args):
        data = self.reader.json_read(DataFiles.PROJECT_LIST)
        project = self._find_project(data, args.name)

        if (project == None):
            print('Такого проекта нет!')
        else:
            data.remove(project)
            self.reader.json_write(DataFiles.PROJECT_LIST, data)
        exit(0)

    def _list(self, args):
        projects = self.reader.json_read(DataFiles.PROJECT_LIST)

        if projects != []:
            print('Алиасы выших пректов:')
            for project in projects:
                print(project['name'])
        else:
            print('Вы ещё не добавили проекты')
        exit(0)

    def _start(self, args):
        project = Application._find_project(self.reader.json_read(DataFiles.PROJECT_LIST), args.name)
        strategy = self.strategyManager.get_strategy(project['type'])

        if (project == None):
            print('Такого проекта нет!')
            exit(0)

        strategy.start(project)
        exit(0)

    @staticmethod
    def _find_project(array, value):
        for item in array:
            if item["name"] == value:
                return item
