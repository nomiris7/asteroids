import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (bullets, updatable, drawable)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        

        asteroids_list = list(asteroids)
        for i in range(len(asteroids_list)):
            if asteroids_list[i].check_collision(player):
                print("Game over!")
            destroyed = False
            for bullet in bullets:
                if asteroids_list[i].check_collision(bullet):
                    print("Hit!")
                    asteroids_list[i].kill_circle()
                    bullet.kill_circle()
                    destroyed = True
                    break
            if destroyed:
                break
            for j in range(i+1, len(asteroids_list)):
                check = asteroids_list[i].check_collision(asteroids_list[j])
                if check:
                    asteroids_list[i].reflect_angle(asteroids_list[j])
        
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()