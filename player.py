import settings
import entity
import pygame

class Player(entity.Entity):
  def __init__(self):
    super().__init__(60, 0.5, r'C:\pp1\labs\aziza python\race\images\cars\car_green.png', settings.SPEED * 4)
    self.rect.center = (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 100)

  def move(self):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
      if(self.rect.left > 0) :
        self.rect.move_ip(-self.MOVEMENT_SPEED, 0)
    if pressed[pygame.K_RIGHT]:
      if(self.rect.right < settings.SCREEN_WIDTH) :
        self.rect.move_ip(self.MOVEMENT_SPEED, 0)
