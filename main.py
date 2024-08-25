import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  fps_counter = pygame.time.Clock()
  delta_time = 0
  updateable = pygame.sprite.Group()
  renderable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updateable, renderable)
  Asteroid.containers = (asteroids, updateable, renderable)
  AsteroidField.containers = (updateable)
  Shot.containers = (updateable, renderable, shots)
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroid_field = AsteroidField()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for obj in updateable:
      obj.update(delta_time)

    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        print("Game over!")
        return
      for shot in shots:
        if shot.is_colliding(asteroid):
          shot.kill()
          asteroid.split()


    screen.fill("black")

    for obj in renderable:
      obj.draw(screen)

    pygame.display.flip()

    delta_time = fps_counter.tick(60) * 0.001


if __name__ == "__main__":
  main()

