from module import Commands, Utils


def run_commands():
    # Commands.read_alarms()
    # Commands.read_current_joint_coordinate_position()
    # Commands.read_current_specified_coordinate_system_position('0', '0')
    Commands.read_status()
    # Commands.read_current_job_details()
    # Commands.write_hold('0')  # 1 on, 0 off
    # Commands.write_reset()
    # Commands.write_cancel()
    # Commands.write_servo_power('0')  # 1 on, 0 off
    # Commands.write_start_job('')  # empty means default set execution job

    # Commands.write_linear_move(
    #     '0', '20', '0',
    #     '353.769', '202.779', '120.658', '-1.34', '35.78', '27.84',
    #     str(Utils.binary_to_decimal(0x00000001)),
    #     '0', '0', '0', '0', '0', '0', '0'
    # )

run_commands()
