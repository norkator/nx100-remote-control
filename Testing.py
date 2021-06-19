"""
This is used for development, individual command testing
"""


from module import Commands, Utils, Gripper
from objects import MoveL, IO


def start_app():
    # Commands.read_alarms()
    # Commands.read_current_joint_coordinate_position()
    # Commands.read_current_specified_coordinate_system_position('0', '0')
    # Commands.read_status()
    # Commands.read_current_job_details()
    # Commands.write_hold('0')  # 1 on, 0 off
    # Commands.write_reset()
    # Commands.write_cancel()
    # Commands.write_servo_power('0')  # 1 on, 0 off
    # Commands.write_start_job('')  # empty means default set execution job
    # Commands.write_linear_move(MoveL.MoveL(
    #     0, 20, 0,
    #     353.769, 202.779, 120.658,
    #     -1.34, 35.78, 27.84,
    #     Utils.binary_to_decimal(0x00000001),
    #     0, 0, 0, 0, 0, 0, 0
    # ))
    # Commands.read_all_job_names()
    # Commands.write_master_job('job_name_here')


    # Gripper.write_gripper_close()
    # Gripper.write_gripper_open()
    # Gripper.read_gripper_closed_command_register()

    # Gripper.write_gripper_close()
    print(Gripper.gripper_is_closed())

    # Gripper.read_gripper_hit()



start_app()
