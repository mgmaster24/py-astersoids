import pygame


class SpriteSheet:

  def __init__(self, filename):
    try:
      self.sheet = pygame.image.load(filename).convert_alpha()
    except pygame.error as e:
      print("Unable to load sprite sheet image: {filename}")
      raise SystemExit(e)

  def image_at(self, rectangle, colorkey = None):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size, pygame.SRCALPHA)
    image.blit(self.sheet, (0, 0), rect)
    if colorkey is not None:
      if colorkey == -1:
        colorkey = image.get_at(0,0)
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image
