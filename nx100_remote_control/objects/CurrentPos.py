class CurrentPos(object):

    # Class constructor
    def __init__(self, position_data):
        self.position = position_data.split(',')
        self.x = float(self.position[0])
        self.y = float(self.position[1])
        self.z = float(self.position[2])
        self.tx = float(self.position[3])
        self.ty = float(self.position[4])
        self.tz = float(self.position[5])

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_tx(self):
        return self.tx

    def get_ty(self):
        return self.ty

    def get_tz(self):
        return self.tz
