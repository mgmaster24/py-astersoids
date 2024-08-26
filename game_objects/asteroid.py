import random

import pygame

from constants import ASTEROID_MIN_RADIUS
from game_objects.circleshape import CircleShape
from renderables.sprite import Sprite


class Asteroid(CircleShape):
  def __init__(self, x, y, radius, asteroid_sprites):
    self.asteroid_sprites = asteroid_sprites

    sprite: Sprite = None
    if radius == 60:
      sprite = asteroid_sprites["lg"]
    elif radius == 40:
      sprite = asteroid_sprites["md"]
    else:
      sprite = asteroid_sprites["sm"]

    super().__init__(x, y, radius, sprite)
    self.rotation = 0

  def draw(self, screen: pygame.Surface):
    if self.sprite is not None:
      img = pygame.transform.rotate(self.sprite.image, self.rotation)
      rect = img.get_rect()
      rect.center = self.position
      screen.blit(img, rect)
    #pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt: float):
    self.position += self.velocity * dt
    self.rotation += 10 * dt
    if self.rotation >= 360:
      self.rotation = 0

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    split_angle = random.uniform(20, 50)
    split1_velocity = self.velocity.rotate(split_angle)
    split2_velocity = self.velocity.rotate(-split_angle)
    new_radii = self.radius - ASTEROID_MIN_RADIUS

    a_split1 = Asteroid(self.position.x, self.position.y, new_radii, self.asteroid_sprites)
    a_split1.velocity = split1_velocity * 1.2
    a_split2 = Asteroid(self.position.x, self.position.y, new_radii, self.asteroid_sprites)
    a_split2.velocity = split2_velocity * 1.2

