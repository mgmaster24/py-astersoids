import pygame


class Sprite:
  def __init__(self, name: str, image: pygame.Surface,  color = None):
    self.name = name
    self.image = image
    self.color = color