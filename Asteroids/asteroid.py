import pygame
import random
from logger import log_state, log_event
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            a = self.velocity.rotate(angle)
            b = self.velocity.rotate(0-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_a.velocity = a * 1.2
            new_asteroid_b.velocity = b * 1.2
