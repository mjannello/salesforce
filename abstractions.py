from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, params) -> None:
        self.params = params

    @abstractmethod
    def execute_action(self):
        pass


class AbstractCommandFactory(ABC):
    @abstractmethod
    def create_command(self, cmd_name, **cmd_params):
        pass

