import pygame
from pygame.locals import *
from texture_bank import TextureBank
from player import Player
from ball import Pointer, Murderer, Saver
from random import randrange
from threading import Thread
from time import sleep


class Drifts:
    def __init__(self):
        self._TextureBank = TextureBank
        self._running = True
        self._display = None
        self.size = self.weight, self.height = 800, 600
        self._sprites = {}
        self._clock = pygame.time.Clock()

        self._thread_controller_balls = Thread(target=self.spawner_balls)

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Drifts')
        pygame.display.set_icon(TextureBank['PLAYER'])

        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self._sprites['player'] = Player()
        self._sprites['balls'] = []
        self._thread_controller_balls.start()

    def create_ball(self):
        randomt = randrange(1, 10)
        if 1 <= randomt <= 4:
            ball = Pointer()
        elif 5 <= randomt <= 8:
            ball = Murderer()
        else:
            ball = Saver()
        self._sprites['balls'].append(ball)

    def spawner_balls(self):
        while self._running:
            qt_balls = randrange(1, 3)
            for i in range(0, qt_balls):
                self.create_ball()
            sleep(3)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._sprites['player'].update()
        for sprite in self._sprites['balls']:
            sprite.update()

    def render(self, sprite):
        self._display.blit(sprite.image, sprite.rect)

    def on_render(self):
        self._display.blit(TextureBank['BACKGROUND'], [0, 0])
        self.render(self._sprites['player'])
        for sprite in self._sprites['balls']:
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