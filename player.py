import pygame

from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SHOT_COOLDOWN, PLAYER_SHOT_SPEED,
                       PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS)
from shot import Shot


class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.shot_cooldown = 0

  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def update(self, dt):
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

  def triangle(self):
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right

    return [a, b, c]

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def move(self, dt):
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    forward = forward * (PLAYER_SPEED * dt)
    self.position = self.position + forward

  def shoot(self):
    if (self.shot_cooldown > 0):
      return

    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    forward = pygame.Vector2(0,1).rotate(self.rotation)
    shot.velocity = forward * PLAYER_SHOT_SPEED
    self.shot_cooldown = PLAYER_SHOT_COOLDOWN
