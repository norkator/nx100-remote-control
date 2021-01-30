from module import Commands


def run_commands():
    # Commands.read_alarms()
    # Commands.read_current_joint_coordinate_position()
    # Commands.read_status()
    # Commands.write_hold('0')  # 1 on, 0 off
    # Commands.write_reset()
    # Commands.write_cancel()
    Commands.write_servo_power('1')  # 1 on, 0 off


run_commands()
