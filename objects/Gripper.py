class Gripper(object):

    # Class constructor
    def __init__(self):
        self.is_closed = False
        self.is_acknowledge = False
        self.is_hit = False

    def set_closed_status(self, register_value):
        self.is_closed = True if int(register_value) == 32 else False

    def is_gripper_closed(self):
        return self.is_closed

    def set_acknowledge(self, register_value):
        self.is_acknowledge = True if register_value == '4' else False

    def is_acknowledge(self):
        return self.is_acknowledge

    def set_hit(self, register_value):
        self.is_hit = True if register_value == '4' else False

    def is_hit(self):
        return self.is_hit
