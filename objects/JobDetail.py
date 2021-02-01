class JobDetail(object):

    # Class constructor
    def __init__(self, response):
        self.parts = response.split(',')

    def job_name(self):
        p = 0
        return self.parts[p] if len(self.parts) > p else 'Job name N/A'

    def line_no(self):
        p = 1
        return self.parts[p] if len(self.parts) > p else 'N/A'

    def step_no(self):
        p = 2
        return self.parts[p] if len(self.parts) > p else 'N/A'
