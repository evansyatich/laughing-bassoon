
import Graph	


node_file = open ("mapPennParkNodes.txt")

nodes = {}

for line in node_file.readlines():
	some = line.split("  ")

	nodes[some[0]] = (some[1], some[2][:-2])


node_file.close()

for key in nodes:
	print(key, nodes[key])


edge_file = open ("mapPennParkEdges.txt")

edges = {}

for line in edge_file.readlines():
	some = line.split(" ") 

	edges[some[0]] = some[1]

edge_file.close()

for key in edges:
	print(key, edges[key])

graph = Graph.Graph(nodes)

