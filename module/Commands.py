from module import Socket, Utils
from objects import Command, Status, JobDetail


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
        Command.Command("RPOSC", (coordinate_system + ', ' + include_external_axis))
    )
    Utils.print_response_details(request_alarms)
    # Todo, write response parser


# Reads the status of mode, cycle, operation, alarm error, and servo
def read_status():
    response_data = Socket.exec_single_command(Command.Command("RSTATS", ""))
    Utils.print_response_details(response_data)
    parts = response_data.split(',')
    data_1 = Utils.decimal_to_binary(int(parts[0]))
    data_2 = Utils.decimal_to_binary(int(parts[1]))
    s = Status.Status(data_1, data_2)
    print('Command remote: ' + str(s.is_command_remote()))
    print('Play: ' + str(s.is_play()))
    print('Teach ' + str(s.is_teach()))
    print('Safety speed operation: ' + str(s.is_safety_speed_operation()))
    print('Running: ' + str(s.is_running()))
    print('Auto: ' + str(s.is_auto()))
    print('One cycle: ' + str(s.is_one_cycle()))
    print('Step: ' + str(s.is_step()))
    print('Servo on: ' + str(s.is_servo_on()))
    print('Error occurring: ' + str(s.is_error_occurring()))
    print('Alarm occurring: ' + str(s.is_alarm_occurring()))
    print('Command hold: ' + str(s.is_command_hold()))
    print('External hold: ' + str(s.is_external_hold()))
    print('Programming pendant hold: ' + str(s.is_programming_pendant_hold()))


# Reads the current job name, line No. and step No
def read_current_job_details():
    response_data = Socket.exec_single_command(Command.Command("RJSEQ", ""))
    Utils.print_response_details(response_data)
    return JobDetail.JobDetail(response_data)


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
        motion_speed_selection, motion_speed, coordinate_specification, x, y, z, tx, ty, tz, d_10, d_11, d_12, d_13,
        d_14, d_15, d_16, d_17):
    separator = ', '
    response_data = Socket.exec_single_command(
        Command.Command(
            "MOVL",
            separator.join(
                [motion_speed_selection, motion_speed, coordinate_specification, x, y, z, tx, ty, tz, d_10, d_11, d_12,
                 d_13, d_14, d_15, d_16, d_17]
            )
        )
    )
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else 'Command run successfully!')
