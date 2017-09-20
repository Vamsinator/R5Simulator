import pygame
from time import sleep
class Coin(pygame.sprite.Sprite):
    color = 0
    status = 0
    location = [0, 0]
    def __init__(self, color, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.color = color
        self.status = 1
        self.rect.x = loc[1]
        self.rect.y = loc[0]

    def get_location(self):
        return self.rect.x, self.rect.y

    def get_color(self):
        sleep(0.1)
        return self.color
