class MoveL(object):
    # https://drive.google.com/file/d/11TY9v_Tb5k23DTz9VuEBmj-vJE5Fmc4R/view

    # Class constructor
    def __init__(self, motion_speed_selection, motion_speed, coordinate_specification,
                 x, y, z, tx, ty, tz, d_10, d_11=0, d_12=0, d_13=0, d_14=0, d_15=0, d_16=0, d_17=0):
        self.motion_speed_selection = motion_speed_selection
        self.motion_speed = motion_speed
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
            str(self.motion_speed_selection),
            str(self.motion_speed),
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
