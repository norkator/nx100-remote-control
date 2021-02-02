from module import Socket, Utils
from objects import Command, Status, JobDetail, CurrentPos, Alarm


# Reads the error alarm code
def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM", ""))
    # Utils.print_response_details(request_alarms)
    alarms = Alarm.Alarm(request_alarms)
    print('Alarms: ' + str(alarms.get_alarms()))
    return alarms


# Reads the current position in joint coordinate system
def read_current_joint_coordinate_position():
    response_data = Socket.exec_single_command(Command.Command("RPOSJ", ""))
    Utils.print_response_details(response_data)
    # Todo, write response parser


# Reads the current position in a specified coordinate system.
# The specification with or without external axis can be made
# coordinate_system = 0: Base coordinate, 1: Robot coordinate, 2: User coordinate 1...24
def read_current_specified_coordinate_system_position(coordinate_system, include_external_axis='0'):
    position_response = Socket.exec_single_command(
        Command.Command("RPOSC", (coordinate_system + ', ' + include_external_axis))
    )
    Utils.print_response_details(position_response)
    return CurrentPos.CurrentPos(position_response)


# Reads the status of mode, cycle, operation, alarm error, and servo
def read_status():
    response_data = Socket.exec_single_command(Command.Command("RSTATS", ""))
    Utils.print_response_details(response_data)
    parts = response_data.split(',')
    data_1 = Utils.decimal_to_binary(int(parts[0]))
    data_2 = Utils.decimal_to_binary(int(parts[1]))
    s = Status.Status(data_1, data_2)
    print('Command remote: ' + str(s.is_command_remote()) + ', ' +
          'Play: ' + str(s.is_play()) + ', ' +
          'Teach ' + str(s.is_teach()) + ', ' +
          'Safety speed operation: ' + str(s.is_safety_speed_operation()) + ', ' +
          'Running: ' + str(s.is_running()) + ', ' +
          'Auto: ' + str(s.is_auto()) + ', ' +
          'One cycle: ' + str(s.is_one_cycle()) + ', ' +
          'Step: ' + str(s.is_step()) + ', ' +
          'Servo on: ' + str(s.is_servo_on()) + ', ' +
          'Error occurring: ' + str(s.is_error_occurring()) + ', ' +
          'Alarm occurring: ' + str(s.is_alarm_occurring()) + ', ' +
          'Command hold: ' + str(s.is_command_hold()) + ', ' +
          'External hold: ' + str(s.is_external_hold()) + ', ' +
          'Programming pendant hold: ' + str(s.is_programming_pendant_hold()))
    return s


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
    print('[E] command run failed!' if '0000' not in response_data else '[i] command run successfully!')


# Resets an alarm of manipulator
def write_reset():
    response_data = Socket.exec_single_command(Command.Command("RESET", ""))
    Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else '[i] command run successfully!')


# Cancels an error
def write_cancel():
    response_data = Socket.exec_single_command(Command.Command("CANCEL", ""))
    Utils.print_response_details(response_data)
    print('[E] cancel command run failed!' if '0000' not in response_data else '[i] cancel command run successfully!')


# Turns servo power supply ON/OFF
def write_servo_power(command):
    if command not in '1' and command not in '0':
        print('[E] servo power command can only be 1 (on) or 0 (off)')
        return
    response_data = Socket.exec_single_command(Command.Command("SVON", command))
    Utils.print_response_details(response_data)
    print('[E] servo command run failed!' if '0000' not in response_data else '[i] servo command run successfully!')


# Starts a job
def write_start_job(job_name):
    response_data = Socket.exec_single_command(Command.Command("START", job_name))
    Utils.print_response_details(response_data)
    print(
        '[E] start job command run failed!' if '0000' not in response_data else '[i] start job command run successfully!')


# Moves a manipulator to a specified coordinate position in linear motion
def write_linear_move(move_l):
    move_cmd = move_l.get_command()
    print('[i] move: ' + move_cmd)
    response_data = Socket.exec_single_command(
        Command.Command("MOVL", move_cmd)
    )
    # Utils.print_response_details(response_data)
    print('[E] command run failed!' if '0000' not in response_data else '[i] command run successfully!')
