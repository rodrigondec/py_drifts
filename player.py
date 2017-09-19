from base_renderizable import BaseRenderizable
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        # super().__init__(surface, image)
        self.image = image
        # self.area = screen.get_rect()
        self.rect = (0, 0)
        self.life = 3
        self.score = 0

    def update(self):
        self.rect = pygame.mouse.get_pos()
