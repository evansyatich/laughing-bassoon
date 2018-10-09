
import Graph	

graph = {}

node_file = open ("mapPennParkNodes.txt")

nodes = {}

for line in node_file.readlines():
	some = line.split("  ")

	nodes[some[0]] = (some[1], some[2][:-2])


node_file.close()


for key in nodes:
	graph[key] = []

for key in graph:
	print(key, graph[key])

map_graph = Graph.Graph(graph)


edge_file = open ("mapPennParkEdges.txt")



for line in edge_file.readlines():
	some = line.split(" ") 

	map_graph.add_vertex(some[0])

	for keys in list(graph):
		if(some[0] == keys):
			map_graph.add_edge({some[0], some[1]})
			
			
print(map_graph.edges())

print("and here be the vertices")

print(map_graph.vertices())

edge_file.close()

##lat = input("Please enter lat: ")
##lon = input("Please enter lon: ")




