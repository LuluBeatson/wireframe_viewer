import math
import itertools
import numpy as np
from scipy.spatial.transform import Rotation as rot

class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    def to_vector(self):
        return np.array([self.x, self.y, self.z])

    def from_vector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        
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
                setattr(node, axis, getattr(node, axis)+dist) # change the node objects's attributes

    def scale(self, scale):
        for node in self.nodes:
            node.x *= scale
            node.y *= scale
            node.z *= scale

    def findCentrevec(self): # averages node coords in each dim
        num_nodes = len(self.nodes)
        x = sum([node.x for node in self.nodes])/num_nodes
        y = sum([node.y for node in self.nodes])/num_nodes
        z = sum([node.z for node in self.nodes])/num_nodes
        return np.array([x, y, z])

    # def reflect

    def rotate(self, axis, angle): # caluclates rotation matrix and applies it to the node attributes
        centre = self.findCentrevec()

        if axis == 'x':
            R = rot.from_rotvec([angle, 0, 0])
        elif axis == 'y':
            R = rot.from_rotvec([0, angle, 0])
        elif axis == 'z':
            R = rot.from_rotvec([0, 0, angle])
        else:
            R = rot.from_rotvec([0, 0, 0])
            
        for node in self.nodes:
            node_vec = node.to_vector() - centre
            node_vec = R.apply(node_vec) + centre
            setattr(node, 'x', node_vec[0])
            setattr(node, 'y', node_vec[1])
            setattr(node, 'z', node_vec[2])


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




