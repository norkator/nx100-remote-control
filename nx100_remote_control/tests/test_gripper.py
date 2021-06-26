import unittest
import nx100_remote_control
from nx100_remote_control.module import Gripper


class MyTestCase(unittest.TestCase):
    nx100_remote_control.MOCK_RESPONSE = True  # only possible to test with mock responses

    def test_write_gripper_close(self):
        response = Gripper.write_gripper_close()
        self.assertEqual(response.get_response(), '0')

    def test_write_gripper_open(self):
        response = Gripper.write_gripper_open()
        self.assertEqual(response.get_response(), '0')


if __name__ == '__main__':
    unittest.main()
