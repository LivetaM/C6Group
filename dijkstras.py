from collections import defaultdict, deque
import math

distance = []


#This class handles the creation of a graph for dijkstras algorithm and
#the calculation of the shortes path between the nodes
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}


    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


    def dijkstra(graph, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                try:
                    weight = current_weight + graph.distances[(min_node, edge)]
                except:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path


    def shortest_path(graph, origin, destination):
        visited, paths = Graph.dijkstra(graph, origin)
        full_path = deque()
        _destination = paths[destination]

        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(origin)
        full_path.append(destination)

        return visited[destination], list(full_path)

    def addnodes(self,EngineLocationX,EngineLocationY,CarLocationX,CarLocationY):

        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}


        for i in range (0,2):
            x = (EngineLocationX[i] - CarLocationX)
            y = (EngineLocationY[i] - CarLocationY)
            xy = (x*x) + (y*y)
            distance.append((math.sqrt(xy)))

        for node in ['Car', 'point1', 'point2', 'Engine']:
            self.add_node(node)

        self.add_edge('Car', 'point1', 0)
        self.add_edge('Car', 'point2', 0)
        self.add_edge('point1', 'Engine', int(distance[0]))
        self.add_edge('point2', 'Engine', int(distance[1]))

        return self.shortest_path('Car', 'Engine')

#This function resets all data given to dijkstras allowing for a new graph
#to be made and new information to be provided
    def clearnodes(self):
        self.nodes = None
        self.edges = None
        self.distances = None
        distance.clear()

