import pygame

from constants import *
from game_objects.asteroid import Asteroid
from game_objects.asteroidfield import AsteroidField
from game_objects.player import Player
from game_objects.shot import Shot
from renderables.sprite_collection import SpriteCollection


def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  game_sprites = SpriteCollection()
  game_sprites.load_sprites("asteroids-arcade.png")

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
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, game_sprites.getPlayerSprites())
  asteroid_field = AsteroidField(game_sprites.getAsteroidSprites())
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

