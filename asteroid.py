from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def update(self,dt):
        self.position = self.position + self.velocity * dt
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def reflect_angle(self, other):
        normal = other.position - self.position
        
        overlap = (self.radius +other.radius - normal.length())/2
        self.position -= normal.normalize() * overlap
        other.position += normal.normalize() * overlap


        self.velocity = self.velocity.reflect(normal)
        other.velocity = other.velocity.reflect(normal)
    
    def kill_circle(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = v1
        asteroid_2.velocity = v2