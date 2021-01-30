from module import Socket
from objects import Command


def run_commands():
    commands = []

    commands.append(Command.Command(""))

    Socket.exec_commands(commands)


run_commands()
