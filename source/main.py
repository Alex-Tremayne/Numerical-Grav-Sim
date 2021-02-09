# These imports tell python that we want to use code from our other files
import particle
import physics

# These imports are from installed python packages
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

# This is a function
# Functions in code work much like a mathematical function
# First we begin by telling the code what the functions takes as inputs
def initialise(num_particles, bounds, velocity, mass, radius=1):
	'''
	def : short for define, this is how all functions start

	initialise : this is the name we give the funciton, it can be anything,  
		as long as there are no spaces. 

	num_particles, bounds, velocity, mass : These are the inputs to the function,
		it will not be able to do anything if they are not provided

	radius=1 : this is also an input, however by setting it equal to 1, we have
		provided it with a default value, so we don't need to pass anything in unless we want a different value
	
	This is everything we need to set up the inputs of a python function. All these inputs will be 
		accessible as variables inside the function body

	Next we write code that tells the function how to turn the inputs into output(s)

	'''

	assert bounds.size == velocity.size # This is just to check that the dimensions are the same

	particles = np.array([]) # Create an empty numpy array, numpy arrays are fast and very feature packed!

	for x in range(num_particles): # This is a loop, it will run num_particles times, 
								   # each time it loops x will increase by 1 until it reaches num_particles-1
								   # x starts with a value of 0
		#print(x)
		temp = particle.particle(np.multiply(bounds, np.random.rand(bounds.size)), np.copy(velocity), mass, radius)
			# Here we create a temporary particle
		particles = np.append(particles, temp) # We then stick it on the end of the particles array

	'''
	Everything above here is an intermediate step. In this case, it is creating a variable called particles
	When it's finished, we need to tell the function that we would like to use it as the output.
	
	This is done using the "return" keyword, essentially saying return this object to whatever called the function

	'''

	return particles




# Here we use the initialise function to define an array of particles
particles = initialise(10, np.array([10.0, 10.0]), np.array([0.0, 0.0]), 100.0)


for item in particles: # This loop just spits out the starting coordinates of the particles, just to check everything worked
	print(item.coord)

# To create the animation, we need a figure and a camera
fig = plt.figure()
camera = Camera(fig) # The camera will make an animation by sticking the figures together and saving it

for x in range(6000): 
	

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
animation.save('grav_sim.gif', fps=600)
