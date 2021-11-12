from abc import ABC, abstractmethod
import os


class Command(ABC):
    @abstractmethod
    def execute_action(self):
        pass

    @staticmethod
    def validate_parameters_existence(params):
        if not params:
            print('invalid command')
            raise Exception('')


class Ls(Command):
    def execute_action(*params):

        path = os.getcwd()
        print(os.listdir(path))
        # TODO: recursion


class Mkdir(Command):
    def execute_action(*params):
        Command.validate_parameters_existence(params)
        directory = params[0]
        if os.path.isdir(directory):
            print('Directory already exists')
            return
        os.mkdir(directory)


class Cd(Command):
    def execute_action(*params):
        Command.validate_parameters_existence(params)

        final_directory = params[0]
        if not os.path.isdir(final_directory):
            print('Invalid directory')
            return
        os.chdir(final_directory)


class Quit(Command):
    def execute_action(*params):
        exit()


class Touch(Command):
    def execute_action(*params):
        file_name = params[0]
        with open(file_name, mode='a'):
            return


class Pwd(Command):
    def execute_action(*params):
        print(os.getcwd())


possible_commands = {    # this could be replace with a Command Factory
    'ls': Ls,
    'mkdir': Mkdir,
    'cd': Cd,
    'quit': Quit,
    'touch': Touch,
    'pwd': Pwd
}


class CommandParser:
    @staticmethod
    def parse(command_string):
        params = command_string.split()
        cmd_name = params.pop(0)
        cmd = possible_commands.get(cmd_name)
        if not cmd:
            print('Unrecognized command')
            raise Exception
        cmd.execute_action(' '.join(params))


if __name__ == '__main__':

    while True:
        line = input()
        if not line:
            continue
        CommandParser.parse(command_string=line)



