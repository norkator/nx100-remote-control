from module import Commands
from objects import IO

# first network input signal
GRIPPER_OPEN_CLOSE_SIGNAL = 22010


def write_gripper_close():
    io_out = IO.IO(GRIPPER_OPEN_CLOSE_SIGNAL, 8)  # each signal line has 8 bits, write them all
    io_out.set_first_eight_io_contracts('00000100')
    Commands.write_io_signals(io_out)


def write_gripper_open():
    io_out = IO.IO(GRIPPER_OPEN_CLOSE_SIGNAL, 8)  # each signal line has 8 bits, write them all
    io_out.set_first_eight_io_contracts('00000000')
    Commands.write_io_signals(io_out)


def read_gripper_
Commands.read_io_signals(IO.IO(10022, 4))