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
location_array = [[130, 130], [130, 605], [180, 175], [180, 550], [225, 225], [225, 500], [270, 275], [270, 455], [365, 130], [365, 180], [365, 225], [365, 270], [365, 460], [365, 505], [365, 555], [365, 600], [460, 275],[460, 460], [505, 220], [505, 505], [545, 175], [545, 550], [600, 130], [600, 605]]  
size = (width, height) = background_image.get_size()
screen = pygame.display.set_mode(size)
coin_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(24):
    coin = Coin(0, location_array[i])
    coin.rect.x, coin.rect.y = coin.get_location()
    coin_list.add(coin)
    all_sprites_list.add(coin)
turtle = Robot()

all_sprites_list.add(turtle)
def progress_sim():
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(background_image, background_rect)
    all_sprites_list.draw(screen)
    turtle.move_using_vector(20, -1.57)
    pygame.display.flip()
progress_sim()
progress_sim()
def quit_sim():
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)
