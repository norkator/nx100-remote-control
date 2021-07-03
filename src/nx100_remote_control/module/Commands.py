from nx100_remote_control.objects import Command, Status, JobDetail, CurrentPos, Alarm, Response
from nx100_remote_control.module import Socket, Utils
import logging
import time


# Reads the error alarm code
def read_alarms():
    request_alarms = Socket.exec_single_command(Command.Command("RALARM", ""))
    # Utils.print_response_details(request_alarms)
    alarms = Alarm.Alarm(request_alarms)
    logging.info('Alarms: ' + str(alarms.get_alarms()))
    return alarms


# Reads the current position in joint coordinate system
def read_current_joint_coordinate_position():
    response_data = Socket.exec_single_command(Command.Command("RPOSJ", ""))
    Utils.print_response_details(response_data)
    return response_data


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
    logging.info('Command remote: ' + str(s.is_command_remote()) + ', ' +
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
        logging.error('[E] hold command can only be 1 (on) or 0 (off)')
        return
    response = Response.Response(Socket.exec_single_command(Command.Command("HOLD", command)))
    Utils.print_response_details(response.get_response())
    logging.info('[i] hold command run successfully!' if response.is_success() else '[E] hold command run failed!')
    return response


# Resets an alarm of manipulator
def write_reset():
    response = Response.Response(Socket.exec_single_command(Command.Command("RESET", "")))
    Utils.print_response_details(response.get_response())
    logging.info('[i] reset command run successfully!' if response.is_success() else '[E] reset command run failed!')
    return response


# Cancels an error
def write_cancel():
    response = Response.Response(Socket.exec_single_command(Command.Command("CANCEL", "")))
    Utils.print_response_details(response.get_response())
    logging.info('[i] cancel command run successfully!' if response.is_success() else '[E] cancel command run failed!')
    return response


# Turns servo power supply ON/OFF
def write_servo_power(command):
    if command not in '1' and command not in '0':
        logging.error('[E] servo power command can only be 1 (on) or 0 (off)')
        return
    response = Response.Response(Socket.exec_single_command(Command.Command("SVON", command)))
    Utils.print_response_details(response.get_response())
    logging.info('[i] servo command run successfully!' if response.is_success() else '[E] servo command run failed!')
    return response


# Starts a job
def write_start_job(job_name):
    response = Response.Response(Socket.exec_single_command(Command.Command("START", job_name)))
    Utils.print_response_details(response.get_response())
    logging.info(
        '[i] start job command run successfully!' if response.is_success() else '[E] start job command run failed!')
    return response


# Moves a manipulator to a specified coordinate position in linear motion
def write_linear_move(move_l):
    move_cmd = move_l.get_command()
    logging.info('[i] move: ' + move_cmd)
    response = Response.Response(Socket.exec_single_command(
        Command.Command("MOVL", move_cmd)
    ))
    # Utils.print_response_details(response_data)
    logging.info('[i] command run successfully!' if response.is_success() else '[E] command run failed!')
    return response


# Moves a manipulator to a specified coordinate position in joint motion.
def write_joint_motion_move(move_j):
    move_cmd = move_j.get_command()
    logging.info('[i] move: ' + move_cmd)
    response = Response.Response(Socket.exec_single_command(
        Command.Command("MOVJ", move_cmd)
    ))
    logging.info('[i] command run successfully!' if response.is_success() else '[E] command run failed!')
    return response


# Is robot in target point function with callback. Timeout given in seconds
def robot_in_target_point_callback(move_l, timeout=10, _callback_success=None, _callback_failed=None):
    current = 0
    for x in range(timeout):
        time.sleep(1)
        cp = read_current_specified_coordinate_system_position(  # returns CurrentPos object
            str(move_l.get_coordinate_specification), '0'
        )
        if Utils.is_in_position(move_l, cp):
            if _callback_success:
                _callback_success()
                break
            else:
                return True
        else:
            current = current + 1
            if current == timeout:
                if _callback_failed:
                    _callback_failed()
                    break
                else:
                    return False


# Reads I/O signals, contact point No. to start read-out, the number of contact points to be read out
def read_io_signals(io):
    response = Response.Response(Socket.exec_single_command(
        Command.Command("IOREAD", io.get_io_read_command())
    ))
    Utils.print_response_details(response.get_response())
    logging.info(
        '[i] IO read command run successfully!' if response.is_success() else '[E] IO read command run failed!')
    return response


# Write I/O signals
def write_io_signals(io):
    response = Response.Response(Socket.exec_single_command(
        Command.Command("IOWRITE", io.get_io_write_command()))
    )
    Utils.print_response_details(response.get_response())
    logging.info(
        '[i] IO write command run successfully!' if response.is_success() else '[E] IO write command run failed!')
    return response


# Read all registered job names
def read_all_job_names():
    response = Response.Response(Socket.exec_single_command(
        Command.Command("RJDIR", "*"))  # * means to read all registered jobs
    )
    Utils.print_response_details(response.get_response())
    logging.info('[i] Read job names command run successfully!' if response.is_success()
                 else '[E] Read job names command run failed!')
    return response


# Set wanted job as master job
def write_master_job(job_name):
    response = Response.Response(Socket.exec_single_command(Command.Command("SETMJ", job_name)))
    Utils.print_response_details(response.get_response())
    logging.info('[i] set master job command run successfully!' if response.is_success()
                 else '[E] set master job command run failed!')
    return response
