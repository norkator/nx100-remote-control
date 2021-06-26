"""
IO network input and output range is start 22010 and ends to signal 23287
"""


class IO(object):

    # Class constructor
    def __init__(self, contact_point_start_no, num_of_contact_points=8):
        self.contact_point_start_no = contact_point_start_no
        self.num_of_contact_points = num_of_contact_points
        self.first_eight_contacts_in = ''

    def get_io_read_command(self):
        return str(self.contact_point_start_no) + ', ' + str(self.num_of_contact_points)

    # Input example, '00000000'
    def set_first_eight_io_contracts(self, eight_contacts_data):
        self.first_eight_contacts_in = eight_contacts_data

    def get_io_write_command(self):
        return str(self.contact_point_start_no) + ', ' + \
               str(self.num_of_contact_points) + ', ' + \
               str(self.first_eight_contacts_in)
