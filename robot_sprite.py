import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Robot.png")
        self.rect = self.image.get_rect()


        
