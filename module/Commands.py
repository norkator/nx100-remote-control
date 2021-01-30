from module import Socket
from objects import Command


# commands = []
# commands.append(Command.Command(""))

# Reads the error alarm code
def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM", ""))
    Socket.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the current position in joint coordinate system.
def read_current_joint_coordinate_position():
    request_alarms = Socket.exec_single_command(Command.Command("RPOSJ", ""))
    Socket.print_response_details(request_alarms)
    # Todo, write response parser
