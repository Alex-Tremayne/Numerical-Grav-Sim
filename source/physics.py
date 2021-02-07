import numpy as np

def eulerSemiImplicit(grav_const, time_step, particles):
	for particle1 in range(len(particles)):
		particles[particle1].acceleration[:] = 0
		for particle2 in range(len(particles)):
			if particle1 != particle2:
				displacement = particles[particle2].coord - particles[particle1].coord
				distance = np.sum(displacement**2)**0.5

				particles[particle1].acceleration += grav_const * particles[particle2].mass * displacement / (distance**3)

		particles[particle1].velocity += particles[particle1].acceleration * time_step
		particles[particle1].coord += particles[particle1].velocity * time_step
