from module import Socket, Utils
from objects import Command


# commands = []
# commands.append(Command.Command(""))

# Reads the error alarm code
def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM", ""))
    Utils.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the current position in joint coordinate system
def read_current_joint_coordinate_position():
    request_alarms = Socket.exec_single_command(Command.Command("RPOSJ", ""))
    Utils.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the current position in a specified coordinate system.
# The specification with or without external axis can be made
def read_current_specified_coordinate_system_position(coordinate_system):
    print('not implemented')
    # request_alarms = Socket.exec_single_command(Command.Command("RPOSC", ""))
    # Utils.print_response_details(request_alarms)
    # Todo, implement coordinate commands, write response parser


# Reads the status of mode, cycle, operation, alarm error, and servo
def read_status():
    request_alarms = Socket.exec_single_command(Command.Command("RSTATS", ""))
    parts = request_alarms.replace('b\'', '').replace('\\r\'', '').split(',')
    data_1 = Utils.decimal_to_binary(int(parts[0]))
    data_2 = Utils.decimal_to_binary(int(parts[1]))
    print(data_1)
    print(data_2)
    # Todo, parse binary data
