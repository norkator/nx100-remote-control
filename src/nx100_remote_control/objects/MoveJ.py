class MoveJ(object):

    """
    !!! WARNING !!!
    !!! motion_speed_percentage 100% could be dangerous !!!
    !!! robot can do very quick movements !!!
    """

    # coordinate_specification options
    coordinate_specification_base_coordinate = 0  # base coordinate option
    coordinate_specification_robot_coordinate = 1  # robot coordinate option
    coordinate_specification_user_1_coordinate = 2  # user 1 coordinate option

    # Class constructor
    def __init__(self, motion_speed_percentage, coordinate_specification,
                 x, y, z, tx, ty, tz, d_10, d_11=0, d_12=0, d_13=0, d_14=0, d_15=0, d_16=0, d_17=0):
        self.motion_speed_percentage = motion_speed_percentage
        self.coordinate_specification = coordinate_specification
        self.x = x
        self.y = y
        self.z = z
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.d_10 = d_10
        self.d_11 = d_11
        self.d_12 = d_12
        self.d_13 = d_13
        self.d_14 = d_14
        self.d_15 = d_15
        self.d_16 = d_16
        self.d_17 = d_17

    def get_command(self):
        separator = ', '
        return separator.join([
            str(self.motion_speed_percentage),
            str(self.coordinate_specification),
            str(self.x),
            str(self.y),
            str(self.z),
            str(self.tx),
            str(self.ty),
            str(self.tz),
            str(self.d_10),
            str(self.d_11),
            str(self.d_12),
            str(self.d_13),
            str(self.d_14),
            str(self.d_15),
            str(self.d_16),
            str(self.d_17)
        ])

    def get_coordinate_specification(self):
        return self.coordinate_specification

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
