import wireframe
import pygame

from examples import make_cube

class ProjectionViewer:
	""" Displays 3D objects on a Pygame screen """

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Wireframe Display')
		self.background = (10,10,50)
		self.wireframes = {}
		self.displayNodes = True
		self.displayEdges = True
		self.nodeColour = (255,50,150)
		self.edgeColour = (255,255,10)
		self.nodeRadius = 4


	def run(self):
		""" Create a pygame screen until it is closed """
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				elif event.type == pygame.KEYDOWN:
					if event.key in key_to_function:
						key_to_function[event.key](self)

			self.display()
			pygame.display.flip()

	def addWireframe(self, name, wireframe):
		""" Add a named wireframe object """
		self.wireframes[name] = wireframe

	def display(self):
		""" Draw the wireframe on the screen using a flat projection onto the xy plane """
		self.screen.fill(self.background)

		for wireframe in self.wireframes.values():
			if self.displayEdges:
				for edge in wireframe.edges:
					pygame.draw.aaline(self.screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)

			if self.displayNodes:
				for node in wireframe.nodes:
					pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)

	def translateAll(self, axis, d): # Translate all wireframes
		for wireframe in self.wireframes.values():
			wireframe.translate(axis, d)

	def scaleAll(self, scale):
		for wireframe in self.wireframes.values():
			wireframe.scale(scale)

	def rotateAll(self, axis, angle):
		""" Rotate all wireframe about their centre, along a given axis by a given angle. """
		for wireframe in self.wireframes.values():
		    wireframe.rotate(axis, angle)


key_to_function = {
	pygame.K_LEFT:   (lambda x: x.translateAll('x', -10)),
	pygame.K_RIGHT:  (lambda x: x.translateAll('x',  10)),
	pygame.K_DOWN:   (lambda x: x.translateAll('y',  10)),
	pygame.K_UP:     (lambda x: x.translateAll('y', -10)),
	pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
	pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8)),
	pygame.K_q: (lambda x: x.rotateAll('x',  0.1)),
	pygame.K_w: (lambda x: x.rotateAll('x', -0.1)),
	pygame.K_a: (lambda x: x.rotateAll('y',  0.1)),
	pygame.K_s: (lambda x: x.rotateAll('y', -0.1)),
	pygame.K_z: (lambda x: x.rotateAll('z',  0.1)),
	pygame.K_x: (lambda x: x.rotateAll('z', -0.1))}

if __name__ == '__main__':
	pv = ProjectionViewer(400, 300)
	cube = make_cube(200, 50)
	pv.addWireframe('cube', cube) # imported from examples.py
	pv.run()
	pv.display()