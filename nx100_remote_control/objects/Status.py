class Status(object):

    # Class constructor
    def __init__(self, data_1, data_2):
        self.data_1 = list(data_1.replace('0b', ''))
        self.data_2 = list(data_2.replace('0b', ''))

    def is_command_remote(self):
        p = 0
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_play(self):
        p = 1
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_teach(self):
        p = 2
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_safety_speed_operation(self):
        p = 3
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_running(self):
        p = 4
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_auto(self):
        p = 5
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_one_cycle(self):
        p = 6
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_step(self):
        p = 7
        return (self.data_1[p] == '1') if len(self.data_1) > p else False

    def is_servo_on(self):
        p = 1
        return (self.data_2[p] == '1') if len(self.data_2) > p else False

    def is_error_occurring(self):
        p = 2
        return (self.data_2[p] == '1') if len(self.data_2) > p else False

    def is_alarm_occurring(self):
        p = 3
        return (self.data_2[p] == '1') if len(self.data_2) > p else False

    def is_command_hold(self):
        p = 4
        return (self.data_2[p] == '1') if len(self.data_2) > p else False

    def is_external_hold(self):
        p = 5
        return (self.data_2[p] == '1') if len(self.data_2) > p else False

    def is_programming_pendant_hold(self):
        p = 6
        return (self.data_2[p] == '1') if len(self.data_2) > p else False
