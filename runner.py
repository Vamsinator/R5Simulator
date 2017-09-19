import pygame, sys

pygame.init()
background_image = pygame.image.load("RegionVField.png")
background_image = pygame.transform.scale(background_image, [750, 750])
background_rect = background_image.get_rect()

size = (width, height) = background_image.get_size()
screen = pygame.display.set_mode(size)

def update_field():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        screen.blit(background_image, background_rect)
        pygame.display.flip()
