from module import Socket, Utils
from objects import Command


# Reads the error alarm code
def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM", ""))
    Utils.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the current position in joint coordinate system
def read_current_joint_coordinate_position():
    response_data = Socket.exec_single_command(Command.Command("RPOSJ", ""))
    Utils.print_response_details(response_data)
    # Todo, write response parser


# Reads the current position in a specified coordinate system.
# The specification with or without external axis can be made
# coordinate_system = 0: Base coordinate, 1: Robot coordinate, 2: User coordinate 1...24
def read_current_specified_coordinate_system_position(coordinate_system, include_external_axis='0'):
    request_alarms = Socket.exec_single_command(
        Command.Command("RPOSC", (coordinate_system + ' ' + include_external_axis))
    )
    Utils.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the status of mode, cycle, operation, alarm error, and servo
def read_status():
    response_data = Socket.exec_single_command(Command.Command("RSTATS", ""))
    parts = response_data.replace('b\'', '').replace('\\r\'', '').split(',')
    data_1 = Utils.decimal_to_binary(int(parts[0]))
    data_2 = Utils.decimal_to_binary(int(parts[1]))
    print(data_1)
    print(data_2)
    # Todo, parse binary data


# Turns HOLD ON/OFF
def write_hold(command):
    if command not in '1' and command not in '0':
        print('[E] hold command can only be 1 (on) or 0 (off)')
        return
    response_data = Socket.exec_single_command(Command.Command("HOLD", command))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')


# Resets an alarm of manipulator
def write_reset():
    response_data = Socket.exec_single_command(Command.Command("RESET", ""))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')


# Cancels an error
def write_cancel():
    response_data = Socket.exec_single_command(Command.Command("CANCEL", ""))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')


# Turns servo power supply ON/OFF
def write_servo_power(command):
    if command not in '1' and command not in '0':
        print('[E] servo power command can only be 1 (on) or 0 (off)')
        return
    response_data = Socket.exec_single_command(Command.Command("SVON", command))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')


# Starts a job
def write_start_job(job_name):
    response_data = Socket.exec_single_command(Command.Command("START", job_name))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')


# Moves a manipulator to a specified coordinate position in linear motion
def write_linear_move(
        motion_speed_selection, motion_speed, coordinate_specification,
        x, y, z, tx, ty, tz,
        d_10, d_11, d_12, d_13, d_14, d_15, d_16, d_17
):
    # response_data = Socket.exec_single_command(Command.Command("MOVL", ...))
    # Utils.print_response_details(response_data)
    # print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')
    print('not implemented')