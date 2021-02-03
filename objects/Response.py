# normal style responses like 0000
class Response(object):

    # Class constructor
    def __init__(self, response):
        self.response = response

    def get_response(self):
        return self.response

    def is_success(self):
        return False if '0000' not in self.response else True
