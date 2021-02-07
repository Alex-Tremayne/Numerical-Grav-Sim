import particle
import physics
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera


def initialise(num_particles, bounds, velocity, mass, radius=1):
	assert bounds.size == velocity.size

	particles = np.array([])

	for x in range(num_particles):
		#print(x)
		temp = particle.particle(np.multiply(bounds, np.random.rand(bounds.size)), np.copy(velocity), mass, radius)
		particles = np.append(particles, temp)

	return particles





particles = initialise(100, np.array([10.0, 10.0]), np.array([0.0, 0.0]), 100.0)


for item in particles:
	print(item.coord)

fig = plt.figure()
camera = Camera(fig)

for x in range(500): 
	

	physics.eulerSemiImplicit(1, 0.001, particles)

	# Get coords
	coords = np.asarray([item.coord for item in particles])
	x, y = coords.T

	plt.plot(x, y, "o", color="blue")
	plt.xlim(0,10)
	plt.ylim(0,10)
	camera.snap()

animation = camera.animate()
 
#Saving the animation
animation.save('grav_sim.gif')
