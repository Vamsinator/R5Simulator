import pygame
import numpy

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Robot.png")
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 550

    def move_using_vector(self, distance, angle):
       self.rect.x += int(numpy.cos(angle)*distance)
       self.rect.y += int(numpy.sin(angle)*distance) 
