from module import Socket
from objects import Command


def run_commands():
    # commands = []
    # commands.append(Command.Command(""))

    command = Command.Command("RALARM")
    Socket.exec_single_command(command)


run_commands()
