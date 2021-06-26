class Alarm(object):

    # Class constructor
    def __init__(self, response):
        self.alarms = str(response).split(',')

    # return alarm from wanted position
    def get_alarm(self, position=0):
        return self.alarms[position] if position < 10 else 'N/A'

    def get_alarms(self):
        return self.alarms