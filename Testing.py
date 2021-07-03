"""
This is used for development, individual command testing
"""

import src.nx100_remote_control
from src.nx100_remote_control.module import Commands, WebServer, Utils, JointMove
from src.nx100_remote_control.objects import MoveJ
from src.nx100_remote_control.objects import MoveJ
import logging
import os


def callback_success():
    print('Something was run successfully')


def callback_failed():
    print('Running something has failed')


def start_app():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    src.nx100_remote_control.MOCK_RESPONSE = True
    # WebServer.run(addr="localhost", port=8080)

    Commands.read_alarms()
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
    #     MoveL.MoveL.motion_speed_selection_posture_speed,
    #     5,
    #     MoveL.MoveL.coordinate_specification_base_coordinate,
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
    # print(Gripper.gripper_is_closed())

    # Gripper.read_gripper_hit()

    # move_l = MoveL.MoveL(
    #     MoveL.MoveL.motion_speed_selection_posture_speed,
    #     5,
    #     MoveL.MoveL.coordinate_specification_base_coordinate,
    #     353.769, 202.779, 120.658,
    #     -1.34, 35.78, 27.84,
    #     Utils.binary_to_decimal(0x00000001),
    #     0, 0, 0, 0, 0, 0, 0
    # )
    # Commands.robot_in_target_point_callback(
    #     move_l=move_l, timeout=10, _callback_success=callback_success, _callback_failed=callback_failed
    # )

    # move_l = MoveL.MoveL(
    #     MoveL.MoveL.motion_speed_selection_posture_speed,
    #     5,
    #     MoveL.MoveL.coordinate_specification_base_coordinate,
    #     352.769, 202.779, 120.658,
    #     -1.34, 35.78, 27.84,
    #     Utils.binary_to_decimal(0x00000001),
    #     0, 0, 0, 0, 0, 0, 0
    # )
    # linear_move = LinearMove.LinearMove()
    # linear_move.go(move_l=move_l, wait=True, poll_limit_seconds=10)
    # print('finished')

    move_j = MoveJ.MoveJ(
        25,  # speed %
        MoveJ.MoveJ.coordinate_specification_base_coordinate,
        352.769, 202.779, 120.658,
        -1.34, 35.78, 27.84,
        Utils.binary_to_decimal(0x00000001),
        0, 0, 0, 0, 0, 0, 0
    )
    linear_move = JointMove.JointMove()
    linear_move.go(move_j=move_j, wait=True, poll_limit_seconds=10)


start_app()
