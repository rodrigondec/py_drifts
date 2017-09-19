import pygame
from pygame.locals import *
from texture_bank import TextureBank
from player import Player

class Drifts:
    def __init__(self):
        self._TextureBank = TextureBank
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.player = Player(TextureBank['PLAYER'])

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

    def render(self, sprite):
        self._display_surf.blit(sprite.image, sprite.rect)

    def on_render(self):
        self._display_surf.blit(TextureBank['BACKGROUND'], [0, 0])
        self.render(self.player)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    game = Drifts()
    game.on_execute()