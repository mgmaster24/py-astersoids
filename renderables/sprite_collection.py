import pygame

from renderables.sprite import Sprite
from renderables.sprite_sheet import SpriteSheet


class SpriteCollection:
  def __init__(self):
    self.sprites = []

  def load_sprites(self, filename):
    sprite_sheet = SpriteSheet(filename)

    # Create player sprites
    ship1_rect = (4, 4, 24, 24)
    ship1_img: pygame.Surface = sprite_sheet.image_at(ship1_rect)
    ship1 = Sprite("ship1", ship1_img)
    self.sprites.append(ship1)

    # Create thruster sprites





    # Create explosion sprites



    # Create asteroid spites
    lg_asteroid_rect = (70, 192, 55, 62)
    lg_asteroid_img: pygame.Surface = sprite_sheet.image_at(lg_asteroid_rect)
    lg_asteroid_img = pygame.transform.scale2x(lg_asteroid_img)
    lg_asteroid = Sprite("lg_asteroid", lg_asteroid_img)
    self.sprites.append(lg_asteroid)

    md_asteroid_rect = (132, 194, 28, 28)
    md_asteroid_img: pygame.Surface = sprite_sheet.image_at(md_asteroid_rect)
    md_asteroid_img = pygame.transform.scale_by(md_asteroid_img, 2.5)
    md_asteroid = Sprite("md_asteroid", md_asteroid_img)
    self.sprites.append(md_asteroid)

    sm_asteroid_rect = (206, 209, 19, 20)
    sm_asteroid_img: pygame.Surface = sprite_sheet.image_at(sm_asteroid_rect)
    sm_asteroid_img = pygame.transform.scale2x(sm_asteroid_img)
    sm_asteroid = Sprite("sm_asteroid", sm_asteroid_img)
    self.sprites.append(sm_asteroid)

    # Create bullet sprites
    shot1_rect = (108, 47, 8, 18)
    shot1_img = pygame.Surface = sprite_sheet.image_at(shot1_rect)
    shot1_img = pygame.transform.scale_by(shot1_img, 1.4)
    shot1 = Sprite("shot1", shot1_img)
    self.sprites.append(shot1)

  def getSprite(self, name)-> Sprite:
    for renderable in self.sprites:
      if renderable.name == name:
        return renderable

    return None

  def getPlayerSprites(self):
    player_sprites = {}
    player_sprites["ship1"] = self.getSprite("ship1")
    player_sprites["shot1"] = self.getSprite("shot1")
    return player_sprites

  def getAsteroidSprites(self):
    asteroid_sprites = {}
    asteroid_sprites["lg"] = self.getSprite("lg_asteroid")
    asteroid_sprites["md"] = self.getSprite("md_asteroid")
    asteroid_sprites["sm"] = self.getSprite("sm_asteroid")
    return asteroid_sprites