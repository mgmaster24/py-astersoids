import pygame

from game_objects.circleshape import CircleShape
from renderables.sprite import Sprite


class Shot(CircleShape):
  def __init__(self, x, y, radius, rotation, sprite: Sprite):
    super().__init__(x, y, radius, sprite)
    self.rotation = rotation

  def draw(self, screen):
    if self.sprite is not None:
      img = self.sprite.image.convert_alpha()
      img = pygame.transform.rotate(self.sprite.image, -self.rotation + 180)
      rect = img.get_rect()
      rect.center = self.position
      screen.blit(img, rect)
    #pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
