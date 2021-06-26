import time


class Time(object):

    # Class constructor
    def __init__(self, millis):
        self.millis = millis

    def set_time_now(self, millis):
        self.millis = millis

    def has_seconds_passed(self, seconds):
        return (self.millis + (seconds * 1000)) < self.get_current_millis()

    @staticmethod
    def get_current_millis():
        return round(time.time() * 1000)
