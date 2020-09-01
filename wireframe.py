import math
import itertools

class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        
class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop  = stop


class Wireframe:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNodes(self, nodeList): # Adds to the list of node objects from coords list
        for coord in nodeList:
            self.nodes.append(Node(coord))

    def addEdges(self, edgeindexList): # Adds to the list of edge objects using pairs of indices
        for (start, stop) in edgeindexList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))

    def outputNodes(self):
        print('\n .::::: Nodes :::::. ')
        for i, node in enumerate(self.nodes):
            print(' %d: (%.2f, %.2f, %.2f)' % (i, node.x, node.y, node.z))
            
    def outputEdges(self):
        print('\n .::::: Edges :::::. ')
        for i, edge in enumerate(self.edges):
            print(' %d: (%.2f, %.2f, %.2f)' % (i, edge.start.x, edge.start.y, edge.start.z), 
                'to (%.2f, %.2f, %.2f)' % (edge.stop.x,  edge.stop.y,  edge.stop.z))

    def translate(self, axis, dist):
        if axis in ['x', 'y', 'z']:
            for node in self.nodes:
                setattr(node, axis, getattr(node, axis)+d) # change the node objects's attributes

    def scale(self, scale):
        for node in self.nodes:
            node.x *= scale
            node.y *= scale
            node.z *= scale




def distance(node1, node2):
    return math.sqrt((node1[0]-node2[0])**2 +(node1[1]-node2[1])**2 +(node1[2]-node2[2])**2) 

if __name__ == "__main__":
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)

    edgeindexList = [(a, b) for (a, b) in itertools.combinations(range(8), 2) if distance(cube_nodes[a], cube_nodes[b])==1]
    cube.addEdges(edgeindexList)

    cube.outputNodes()
    cube.outputEdges()


    # print([(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)])

