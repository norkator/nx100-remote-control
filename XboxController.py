from module import xbox360_controller
from module import Commands
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

    # game logic
    #  if playing:
    ball_pos[0] += int(left_x * 5)
    ball_pos[1] += int(left_y * 5)
    # print(str(ball_pos[0]) + ' ' + str(ball_pos[1]))

    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit()
