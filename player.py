import pygame
from texture_bank import TextureBank


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.type = 'PLAYER'
        self.image = pygame.transform.scale(TextureBank[self.type], (45, 45))
        self.area = screen.get_rect()
        self.rect = (0, 0)
        self.life = 3
        self.score = 0

    def update(self):
        self.rect = pygame.mouse.get_pos()

    def reset_life(self):
        self.life = 3

    def reset_score(self):
        self.score = 0

    def inc_score(self, n):
        self.score += n

    def death(self):
        self.life -= 1
