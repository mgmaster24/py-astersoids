import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    split_angle = random.uniform(20, 50)
    split1_velocity = self.velocity.rotate(split_angle)
    split2_velocity = self.velocity.rotate(-split_angle)
    new_radii = self.radius - ASTEROID_MIN_RADIUS

    a_split1 = Asteroid(self.position.x, self.position.y, new_radii)
    a_split1.velocity = split1_velocity * 1.2
    a_split2 = Asteroid(self.position.x, self.position.y, new_radii)
    a_split2.velocity = split2_velocity * 1.2

