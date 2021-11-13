import os

from abstractions import Command
from errors import DirectoryMissing, FileMissing


class Ls(Command):
    def execute_action(self):
        print(' '.join(os.listdir()))
        # TODO: recursion


class Mkdir(Command):
    def __init__(self, params):
        if not params:
            raise DirectoryMissing('Directory is missing')
        super(Mkdir, self).__init__(params)

    def execute_action(self):
        directory = self.params[0]
        if os.path.isdir(directory):
            print('Directory already exists')
            return
        os.mkdir(directory)


class Cd(Command):
    def __init__(self, params):
        if not params:
            raise DirectoryMissing('Directory is missing')
        super(Cd, self).__init__(params)

    def execute_action(self):
        final_directory = self.params[0]
        print(f'final_directory: {final_directory}')
        if not os.path.isdir(final_directory):
            print('Invalid directory')
            return
        os.chdir(final_directory)


class Quit(Command):
    def execute_action(self):
        exit()


class Touch(Command):
    def __init__(self, params):
        if not params:
            raise FileMissing('File is missing')
        super(Touch, self).__init__(params)

    def execute_action(self):
        file_name = self.params[0]
        with open(file_name, mode='a'):
            return


class Pwd(Command):
    def execute_action(self):
        print(os.getcwd())


class UnrecognizedCommand(Command):
    def execute_action(self):
        print('Unrecognized command')
