from errors import DirectoryMissing, FileMissing
from factories import CommandFactory


class CommandParser:

    @staticmethod
    def parse(command_string):
        cmd_factory = CommandFactory()
        input_string_list = command_string.split()
        cmd_name = input_string_list[0]
        cmd_params = input_string_list[1:]
        try:
            return cmd_factory.create_command(cmd_name, *cmd_params)
        except (DirectoryMissing, FileMissing) as exception:
            raise exception


if __name__ == '__main__':

    while True:
        line = input()
        if not line:
            continue
        try:
            cmd = CommandParser.parse(command_string=line)
            cmd.execute_action()
        except (DirectoryMissing, FileMissing) as e:
            print(e.message)





