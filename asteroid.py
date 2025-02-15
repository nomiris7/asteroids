from circleshape import *

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