"""
Commander class for linear moves
"""

from nx100_remote_control.module import Commands, Utils
import time


class LinearMove(object):

    # Class constructor
    def __init__(self):
        self.stopped = False

    def go(self, move_l, wait=True, poll_limit_seconds=30):
        """
        commands robot to move into position linear way

        :param move_l: MoveL object describing target position and move settings
        :param wait: wait for move to complete or not
        :param poll_limit_seconds: functions as a timeout of wait is enabled
        :return: boolean
        """
        self.stopped = False
        Commands.write_hold('0')  # disable hold if currently enabled
        Commands.write_linear_move(move_l=move_l)  # execute wanted move command
        current = 0
        if not wait:
            return True
        for x in range(poll_limit_seconds):
            if self.stopped:
                return False
            time.sleep(1)
            cp = Commands.read_current_specified_coordinate_system_position(  # returns CurrentPos object
                str(move_l.get_coordinate_specification), '0'
            )
            if Utils.is_in_position(move_l, cp):
                return True
            else:
                current = current + 1
                if current == poll_limit_seconds:
                    return False

    def stop(self):
        """
        stop upper go function
        """
        self.stopped = True
        Commands.write_hold('1')  # only way to stop robot from executing move
