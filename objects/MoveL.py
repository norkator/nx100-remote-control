class MoveL(object):
    # https://drive.google.com/file/d/11TY9v_Tb5k23DTz9VuEBmj-vJE5Fmc4R/view

    # motion_speed_selection options
    motion_speed_selection_post_speed = 0  # this option will do fast angle speeds
    motion_speed_selection_posture_speed = 1  # this option does smoother angle speeds defined by motion_speed variable

    # coordinate_specification options
    coordinate_specification_base_coordinate = 0  # base coordinate option
    coordinate_specification_robot_coordinate = 1  # robot coordinate option
    coordinate_specification_user_1_coordinate = 2  # user 1 coordinate option

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
