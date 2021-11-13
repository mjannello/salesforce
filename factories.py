from abstractions import AbstractCommandFactory
from commands import Ls, Mkdir, Cd, Quit, Touch, Pwd, UnrecognizedCommand
from errors import DirectoryMissing, FileMissing


class CommandFactory(AbstractCommandFactory):
    commands = {  # this could be replace with a Command Factory
        'ls': Ls,
        'mkdir': Mkdir,
        'cd': Cd,
        'quit': Quit,
        'touch': Touch,
        'pwd': Pwd
    }

    def create_command(self, cmd_name, *cmd_params):
        cmd = self.commands.get(cmd_name)
        if not cmd:
            return UnrecognizedCommand
        try:
            return cmd(list(cmd_params))
        except (DirectoryMissing, FileMissing) as e:
            raise e



