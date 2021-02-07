import particle
import physics
import numpy as np


def initialise(num_particles, bounds, velocity, mass, radius=1):
	assert bounds.size == velocity.size

	particles = np.array([])

	for x in range(num_particles):
		#print(x)
		temp = particle.particle(np.multiply(bounds, np.random.rand(bounds.size)), velocity, mass, radius)
		particles = np.append(particles, temp)

	return particles





particles = initialise(10, np.array([10.0, 10.0]), np.array([10.0, 10.0]), 10.0)
print(particles.size)
for item in particles:
	print(item.coord)


for x in range(100): 
	physics.eulerSemiImplicit(1,0.001,particles)
	print("Time: " + str(x * 0.001))
	for particle in particles:
		print(particle.coord)