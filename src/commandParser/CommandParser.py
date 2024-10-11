import argparse

from src.dataClass.Parser import SubParser, Param


class CommandParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="CLI-приложение на Python с подкомандами")
        self.subparsers = self.parser.add_subparsers()

    def add_command(self, subparser: SubParser, params: list[Param], func):
        parser_add = self.subparsers.add_parser(subparser.name, help=subparser.help)
        for param in params:
            parser_add.add_argument(param.name, help=param.help)
        parser_add.set_defaults(func=func)

    def execute(self, args):
        arg = self.parser.parse_args(args)
        arg.func(arg)

    def help(self):
        self.parser.print_help()
