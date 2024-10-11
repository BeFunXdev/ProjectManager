from src.strategy.Local import LocalStrategy


class StrategyManager:

    def get_strategy(self, strategy):
        match strategy:
            case 'github':
                pass
            case _:
                return LocalStrategy()
