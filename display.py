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
		self.nodeColour = (255,255,255)
		self.edgeColour = (200,200,200)
		self.nodeRadius = 4


	def run(self):
		""" Create a pygame screen until it is closed """
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

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




if __name__ == '__main__':
	pv = ProjectionViewer(400, 300)
	cube = make_cube(200, 50)
	pv.addWireframe('cube', cube) # imported from examples.py
	pv.run()
	pv.display()