import pygame
import numpy as np
import math

# Define constants
G = 6.67408e-11  # gravitational constant
c = 299792458  # speed of light

# Define Particle class
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, mass, vel, color, size):
        super().__init__()
        self.pos = np.array(pos, dtype=float)
        self.mass = mass
        self.vel = np.array(vel, dtype=float)
        self.color = color
        self.size = size

    def update(self, dt, particles):
        # Calculate acceleration due to gravity
        acc = np.array([0.0, 0.0, 0.0], dtype=float)
        for particle in particles:
            if particle != self:
                r = particle.pos - self.pos
                vel_rel = particle.vel - self.vel
                gamma = 1.0 / math.sqrt(1 - (np.dot(self.vel, self.vel) / (c * c)))
                acc += (G * particle.mass / (gamma ** 3 * np.linalg.norm(r) ** 3)) * r[:, np.newaxis]

        # Update velocity and position
        self.vel += acc * dt
        self.pos += self.vel * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size)

# Define main function
def main():
    # Initialize pygame
    pygame.init()

    # Set up window
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Set up clock
    clock = pygame.time.Clock()

    # Create particles
    particles = []
    particles.append(Particle([size[0] / 2, size[1] / 2], 1.0e5, [0.0, 0.0, 0.0], (255, 255, 255), 10))
    particles.append(Particle([size[0] / 2 + 200, size[1] / 2], 1.0e3, [0.0, 10.0, 0.0], (255, 0, 0), 5))

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Clear screen
        screen.fill((0, 0, 0))

        # Update particles
        dt = clock.tick(60) / 1000.0
        for particle in particles:
            particle.update(dt, particles)
            particle.draw(screen)

        # Update screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
