import pygame
from texture_bank import TextureBank
from random import randrange


class Ball(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.type = type
        self.area = screen.get_rect()
        self.image = pygame.transform.scale(TextureBank[self.type], (45, 45))
        randomx = randrange(0, self.area.w, 5)
        self.rect = (randomx, 0)

        self.accel_x = None
        self.accel_y = None
        randomax = randrange(0, 3)
        self.accel_y = randrange(0, 1)
        if randomax == 0:
            self.accel_x = -1
        elif randomax == 1:
            self.accel_x = 0
        elif randomax == 2:
            self.accel_x = 1

        self.stoped()

    def update(self):
        self.rect = (self.rect[0] + self.accel_x, self.rect[1] + self.accel_y)

    def invert_accel_x(self):
        if randrange(0, 3) == 1:
            if randrange(0, 1) == 1:
                if self.accel_x == -1:
                    self.accel_x = 1
                elif self.accel_x == 0:
                    self.accel_x = 1
                else:
                    self.accel_x = 0
            else:
                if self.accel_x == -1:
                    self.accel_x = 0
                elif self.accel_x == 0:
                    self.accel_x = -1
                else:
                    self.accel_x = -1

    def invert_accel_y(self):
        if randrange(0, 1) == 1:
            if self.accel_y == 1:
                self.accel_y = 0
            else:
                self.accel_y = 1

    def stoped(self):
        if self.accel_x == 0 and self.accel_y == 0:
            self.accel_y = 1


class Pointer(Ball):
    def __init__(self):
        Ball.__init__(self, 'POINTER')
        self.attached = False
        self.bola_to_mouse = None

    def attach(self):
        self.bola_to_mouse = (self.rect, pygame.mouse.get_pos())
        self.attached = True

    def follow_mouse(self):
        x = self.bola_to_mouse[0][0] + (pygame.mouse.get_pos()[0] - self.bola_to_mouse[1][0])
        y = self.bola_to_mouse[0][1] + (pygame.mouse.get_pos()[1] - self.bola_to_mouse[1][1])
        self.rect = (x, y)

    def update(self):
        if self.attached:
            self.follow_mouse()
        else:
            Ball.update(self)


class Murderer(Ball):
    def __init__(self):
        Ball.__init__(self, 'MURDERER')


class Saver(Ball):
    def __init__(self):
        Ball.__init__(self, 'SAVER')
