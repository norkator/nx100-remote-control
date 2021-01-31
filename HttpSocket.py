from module import Commands


def run_commands():
    Commands.read_alarms()
    # Commands.read_current_joint_coordinate_position()
    # Commands.read_current_specified_coordinate_system_position('0', '0')
    # Commands.read_status()
    # Commands.read_current_job_details()
    # Commands.write_hold('0')  # 1 on, 0 off
    # Commands.write_reset()
    # Commands.write_cancel()
    # Commands.write_servo_power('1')  # 1 on, 0 off
    # Commands.write_start_job('')  # empty means default set execution job
    # Commands.write_linear_move()


run_commands()
