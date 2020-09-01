from wireframe import *

def make_cube(scale, buffer):

	cube_nodes = [(x,y,z) for x in (buffer,buffer+scale) for y in (buffer,buffer+scale) for z in (buffer,buffer+scale)]
	cube = Wireframe()
	cube.addNodes(cube_nodes)

	edgeindexList = [(a, b) for (a, b) in itertools.combinations(range(8), 2) if distance(cube_nodes[a], cube_nodes[b])==scale]
	cube.addEdges(edgeindexList)

	cube.outputNodes()
	cube.outputEdges()

	return cube