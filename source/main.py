import particle
import numpy as np


def initialise(num_particles, bounds, velocity, mass, radius=1):
	assert bounds.size == velocity.size

	particles = np.array([])

	for x in range(num_particles):
		#print(x)
		temp = particle.particle(np.multiply(bounds, np.random.rand(bounds.size)), velocity, mass, radius)
		particles = np.append(particles, temp)

	return particles





particles = initialise(10, np.array([10, 10]), np.array([10, 10]), 10)
print(particles.size)
for item in particles:
	print(item.coord)