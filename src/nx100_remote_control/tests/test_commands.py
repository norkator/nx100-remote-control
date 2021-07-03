import unittest
import nx100_remote_control
from nx100_remote_control.module import Commands, Utils
from nx100_remote_control.objects import MoveJ, MoveL, IO


class MyTestCase(unittest.TestCase):
    nx100_remote_control.MOCK_RESPONSE = True  # only possible to test with mock responses

    def test_read_alarms(self):
        alarms = Commands.read_alarms()
        self.assertEqual(alarms.get_alarms(), ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

    def test_read_current_joint_coordinate_position(self):
        position = Commands.read_current_joint_coordinate_position()
        self.assertEqual(position, '45411,-59646,-55567,667,-1077,-1260,0,0,0,0,0,0')

    def test_write_hold(self):
        res = Commands.write_hold('1')
        self.assertEqual(res.get_response(), '0000')

    def test_write_reset(self):
        res = Commands.write_reset()
        self.assertEqual(res.get_response(), '0000')

    def test_write_cancel(self):
        res = Commands.write_cancel()
        self.assertEqual(res.get_response(), '0000')

    def test_write_servo_power(self):
        res = Commands.write_servo_power('1')
        self.assertEqual(res.get_response(), '0000')

    def test_write_start_job(self):
        res = Commands.write_start_job('test_job')
        self.assertEqual(res.get_response(), '0000')

    def test_read_io_signals(self):
        io = IO.IO(4)
        res = Commands.read_io_signals(io)
        self.assertEqual(res.get_response(), '0')

    def test_write_io_signals(self):
        io = IO.IO(4)
        res = Commands.write_io_signals(io)
        self.assertEqual(res.get_response(), '0')

    def test_read_all_job_names(self):
        res = Commands.read_all_job_names()
        self.assertEqual(res.get_response(), '')

    def test_write_master_job(self):
        res = Commands.write_master_job('test_job')
        self.assertEqual(res.get_response(), '0000')

    def test_linear_motion_move(self):
        move_l = MoveL.MoveL(
            MoveL.MoveL.motion_speed_selection_posture_speed,
            5,
            MoveL.MoveL.coordinate_specification_base_coordinate,
            352.769, 202.779, 120.658,
            -1.34, 35.78, 27.84,
            Utils.binary_to_decimal(0x00000001),
            0, 0, 0, 0, 0, 0, 0
        )
        res = Commands.write_linear_move(move_l=move_l)
        self.assertEqual(res.get_response(), '0000')

    def test_joint_motion_move(self):
        move_j = MoveJ.MoveJ(
            25,  # speed %
            MoveJ.MoveJ.coordinate_specification_base_coordinate,
            352.769, 202.779, 120.658,
            -1.34, 35.78, 27.84,
            Utils.binary_to_decimal(0x00000001),
            0, 0, 0, 0, 0, 0, 0
        )
        res = Commands.write_joint_motion_move(move_j=move_j)
        self.assertEqual(res.get_response(), '0000')


if __name__ == '__main__':
    unittest.main()
