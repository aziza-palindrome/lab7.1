import settings
import obstacle

class Coin(obstacle.Obstacle):
  def __init__(self):
    super().__init__(20, 1, r'C:\pp1\labs\aziza python\race\images\coin.png', settings.SPEED)
