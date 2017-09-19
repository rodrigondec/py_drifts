import pygame
from pygame.locals import *
from texture_bank import TextureBank
from player import Player


class Drifts:
    def __init__(self):
        self._TextureBank = TextureBank
        self._running = True
        self._display = None
        self.size = self.weight, self.height = 800, 600
        self._sprites = {}
        self._clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Drifts')
        pygame.display.set_icon(TextureBank['PLAYER'])

        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._sprites['player'] = Player()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for key, sprite in self._sprites.items():
            sprite.update()
        # self._player.update()

    def render(self, sprite):
        self._display.blit(sprite.image, sprite.rect)

    def on_render(self):
        self._display.blit(TextureBank['BACKGROUND'], [0, 0])
        for key, sprite in self._sprites.items():
            self.render(sprite)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self._clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    game = Drifts()
    game.on_execute()