import random
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
	
	def __init__(self, num_of_nodes = 0):
		"""
		Intitailze the no. of nodes in web link, 
					out_degree, adjacency list of each node,
		"""
		self.num_of_nodes = num_of_nodes
		self.num_of_nodes = 0
		self.adj_list = []
		self._out_degree = []
		self.in_link_nodes = []
		self.edges = []

		for i in range(0, num_of_nodes, 1):
			self.adj_list.append([])
			self._out_degree.append(0)
			self.in_link_nodes.append(set())

	
	def add_node(self):
		"""
		Increase no. of nodes in web link by one
		"""
		self.num_of_nodes += 1
		self.adj_list.append([])
		self.in_link_nodes.append([])

	def add_edge(self, u, v):
		"""
		add_edge(u, v) adds a directed edge from node u to node v
		"""
		self.adj_list[u].append(v)
		self._out_degree[u] += 1
		self.in_link_nodes[v].add(u)
		self.edges.append([u, v])

	def visualize(self):
		"""
		Produces a visualization of graph
		"""
		G = nx.DiGraph(directed=True)
		G.add_edges_from(self.edges)

		options = {
		    'node_color': 'blue',
		    'node_size': 500,
		    'width': 2,
		    'arrowstyle': '-|>',
		    'arrowsize': 12,
		}

		nx.draw_networkx(G, **options)

	@property
	def out_degree(self):
		"""
		Getter for _out_degree[]
		"""
		return self._out_degree

	@out_degree.setter
	def out_degree(self, x):
		raise ("can't set attribute")


def generate_graph(nodes, edges):

	"""
	Returns an unweighted, directed graph with no self-loops or multiple edges
	"""
	g = Graph(nodes)
	lt = min(edges, nodes * (nodes - 1))
	cnt = 0
	edge_set = set()

	while(cnt != lt):
		u = random.randint(0, nodes - 1)
		v = random.randint(0, nodes - 1)

		if(u != v and (not (u, v) in edge_set)):
			cnt += 1
			edge_set.add((u, v))
			g.add_edge(u, v)

	g.visualize()
	plt.show()

	return g
