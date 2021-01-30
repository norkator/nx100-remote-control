from module import Socket
from objects import Command


# commands = []
# commands.append(Command.Command(""))

def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM"))
    Socket.print_response_details(request_alarms)

