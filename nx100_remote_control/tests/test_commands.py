import unittest
import nx100_remote_control
from nx100_remote_control.module import Commands


class MyTestCase(unittest.TestCase):
    nx100_remote_control.MOCK_RESPONSE = True  # only possible to test with mock responses

    def test_read_alarms(self):
        alarms = Commands.read_alarms()
        self.assertEqual(alarms.get_alarms(), ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

    def test_read_current_joint_coordinate_position(self):
        position = Commands.read_current_joint_coordinate_position()
        self.assertEqual(position, '45411,-59646,-55567,667,-1077,-1260,0,0,0,0,0,0')


if __name__ == '__main__':
    unittest.main()
