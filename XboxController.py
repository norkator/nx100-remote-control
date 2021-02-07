from module import xbox360_controller, Commands, Utils
from objects import Time, MoveL
import pygame

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# window settings
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("NX100 remote")
FPS = 60
clock = pygame.time.Clock()

# make a controller
controller = xbox360_controller.Controller()

# make a ball
ball_pos = [290, 290]
ball_radius = 10
ball_color = WHITE

done = False

time = Time.Time(Time.Time.get_current_millis())

# robot
SPEED = 50
WAIT_FOR = 0.5  # seconds


def get_position():
    return Commands.read_current_specified_coordinate_system_position('0', '0')


while not done:

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == xbox360_controller.START:
                Commands.write_servo_power('1')
                print('servo on')
            if event.button == xbox360_controller.BACK:
                Commands.write_servo_power('0')
                print('servo off')

            # handle events for specific controllers
            if event.joy == controller.get_id():
                if event.button == xbox360_controller.A:
                    if ball_color == WHITE:
                        ball_color = RED
                    else:
                        ball_color = WHITE

    # handle joysticks
    left_x, left_y = controller.get_left_stick()

    # joystick logic handling
    if left_x < -0.2 or left_x > 0.2:
        if time.has_seconds_passed(WAIT_FOR):
            time.set_time_now(time.get_current_millis())
            c_pos = get_position()
            Commands.write_linear_move(MoveL.MoveL(
                0, SPEED, 0,
                (c_pos.get_x() + int(left_x * 10)),
                c_pos.get_y(),
                c_pos.get_z(), c_pos.get_tx(), c_pos.get_ty(), c_pos.get_tz(),
                Utils.binary_to_decimal(0x00000001)
            ))
            ball_pos[0] += int(left_x * 5)

    if left_y < -0.2 or left_y > 0.2:
        if time.has_seconds_passed(WAIT_FOR):
            time.set_time_now(time.get_current_millis())
            c_pos = get_position()
            Commands.write_linear_move(MoveL.MoveL(
                0, SPEED, 0,
                c_pos.get_x(),
                (c_pos.get_y() - int(left_y * 10)),
                c_pos.get_z(), c_pos.get_tx(), c_pos.get_ty(), c_pos.get_tz(),
                Utils.binary_to_decimal(0x00000001)
            ))
            ball_pos[1] += int(left_y * 5)

    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit()
