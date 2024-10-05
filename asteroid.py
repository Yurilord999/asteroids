import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x ,y ,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2 )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rnd_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position.x, self.position.y, new_radius)
        split2 = Asteroid(self.position.x, self.position.y, new_radius)
        split1.velocity = self.velocity.rotate(rnd_angle) * 1.2
        split2.velocity = self.velocity.rotate(-rnd_angle) * 1.2