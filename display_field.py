import pygame, sys
from coin_sprite import Coin
from robot_sprite import Robot
pygame.init()
clock = pygame.time.Clock()
unscaled_image = pygame.image.load("RegionVField.png")
original_size = unscaled_image.get_rect()
scaling_factor = .708884688090737
background_image = pygame.transform.scale(unscaled_image, [750, 750])
background_rect = background_image.get_rect()

size = (width, height) = background_image.get_size()
screen = pygame.display.set_mode(size)
coin_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(24):
    coin = Coin(0, [130, 130])
    coin.rect.x, coin.rect.y = coin.get_location()
    coin_list.add(coin)
    all_sprites_list.add(coin)
turtle = Robot()
turtle.rect.x, turtle.rect.y = 200, 200
all_sprites_list.add(turtle)
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        screen.blit(background_image, background_rect)
        all_sprites_list.draw(screen)
        pygame.display.flip()
