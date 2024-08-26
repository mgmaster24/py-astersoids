import pygame

from constants import (PLAYER_RADIUS, PLAYER_SHOT_COOLDOWN, PLAYER_SHOT_SPEED,
                       PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS)
from game_objects.circleshape import CircleShape
from game_objects.shot import Shot


class Player(CircleShape):
  def __init__(self, x, y, player_sprites):
    sprite = player_sprites["ship1"]
    super().__init__(x, y, PLAYER_RADIUS, sprite)
    self.rotation = 0
    self.shot_cooldown = 0
    # Scale the image to take
    self.sprite.image = pygame.transform.scale_by(self.sprite.image, 2.0)
    # flip image to be point down initially
    self.sprite.image = pygame.transform.rotate(self.sprite.image, 180)
    self.shot_sprite = player_sprites["shot1"]

  def draw(self, screen: pygame.Surface):
    if self.sprite is not None:
      img = pygame.transform.rotate(self.sprite.image, -self.rotation)
      rect = img.get_rect()
      rect.center = self.position
      screen.blit(img, rect)
    #pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt: float):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
      self.rotate(-dt)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(-dt)
    if keys[pygame.K_SPACE]:
      self.shoot()

    self.shot_cooldown -= dt

  def triangle(self) -> list[pygame.Vector2]:
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right

    return [a, b, c]

  def rotate(self, dt: float):
    self.rotation += PLAYER_TURN_SPEED * dt

  def move(self, dt: float):
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    forward = forward * (PLAYER_SPEED * dt)
    self.position = self.position + forward

  def shoot(self):
    if (self.shot_cooldown > 0):
      return

    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation, self.shot_sprite)
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    shot.velocity = forward * PLAYER_SHOT_SPEED
    self.shot_cooldown = PLAYER_SHOT_COOLDOWN
