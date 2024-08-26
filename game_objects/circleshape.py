import pygame

from renderables.sprite import Sprite


class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x: float, y: float, radius: float, sprite: Sprite = None):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0,0)
    self.radius = radius
    self.sprite = sprite

  def draw(self, screen: pygame.Surface):
    pass

  def update(self, dt: float):
    pass

  def is_colliding(self, obj) -> bool:
    dist = self.position.distance_to(obj.position)
    return dist <= self.radius + obj.radius