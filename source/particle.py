import numpy as np
class particle:

    def __init__(self, coord, velocity, mass, radius):
        self.coord = coord
        self.velocity = velocity
        self.mass = mass
        self.radius = radius
        self.acceleration = np.zeros(len(velocity))
