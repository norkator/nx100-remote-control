from nx100_remote_control.module import Commands
from nx100_remote_control.objects import IO, Gripper
import logging

'''
These signals are this repository end goal specific
following gripper and its signals are custom device not supplied by Motoman
dont run these commands with actual robot with other hardware connected into these signal registers
'''

GRIPPER_OPEN_CLOSE_SIGNAL_INPUT = 22010  # first network input signal (only input method)
GRIPPER_OPEN_CLOSE_SIGNAL = 10022  # Universal Output IO signal register
GRIPPER_ACKNOWLEDGE_SIGNAL = 25  # Universal Input IO signal register
GRIPPER_HIT_SIGNAL = 27  # Universal Input IO signal register


def write_gripper_close():
    io_out = IO.IO(GRIPPER_OPEN_CLOSE_SIGNAL_INPUT, 4)  # each signal line has 8 bits, write them all
    io_out.set_first_eight_io_contracts('00000100')  # Todo, value not decided
    return Commands.write_io_signals(io_out)


def write_gripper_open():
    io_out = IO.IO(GRIPPER_OPEN_CLOSE_SIGNAL_INPUT, 4)  # each signal line has 8 bits, write them all
    io_out.set_first_eight_io_contracts('00000000')  # Todo, value not decided
    return Commands.write_io_signals(io_out)


# gripper closed or open
def read_gripper_closed_command_register():
    gripper_status = Gripper.Gripper()
    gripper_status.set_closed_status(
        Commands.read_io_signals(IO.IO(GRIPPER_OPEN_CLOSE_SIGNAL, 4))
    )
    return gripper_status


# gripper close or open command ack
def read_gripper_acknowledge():
    gripper_status = Gripper.Gripper()
    res = Commands.read_io_signals(IO.IO(GRIPPER_ACKNOWLEDGE_SIGNAL, 1)).get_response()
    logging.info('Gripper ack decimal: ' + res)
    gripper_status.set_closed_status(res)
    return gripper_status.is_gripper_closed()


# same command as upper one but better function name
def gripper_is_closed():
    gripper_status = Gripper.Gripper()
    res = Commands.read_io_signals(IO.IO(GRIPPER_ACKNOWLEDGE_SIGNAL, 1)).get_response()
    logging.info('Gripper ack decimal: ' + res)
    gripper_status.set_closed_status(res)
    return gripper_status.is_gripper_closed()


# gripper hit something signal on or off (this should program set hold or eStop on)
def read_gripper_hit():
    gripper_status = Gripper.Gripper()
    gripper_status.set_closed_status(
        Commands.read_io_signals(IO.IO(GRIPPER_HIT_SIGNAL, 4))
    )
    return gripper_status
