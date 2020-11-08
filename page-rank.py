import graph
import copy

total_nodes = 10 # total no. of nodes
total_edges = 30 # total no. of edges
d = 0.85 # damping factor
total_iterations = 3

def calc_page_rank(prev_rank, in_link_nodes, out_degree):
	new_rank = [(1.0 - d) / total_nodes] * total_nodes
	rank_sum = 0.0

	# Calculate new rank for each node
	for node in range(0, total_nodes, 1):

		# iterate all incoming_node such that there's an edge incoming_node -> node
		for incoming_node in in_link_nodes[node]:
			# PR(x) = (1 - d)/N + d * (for each edge y -> x, PR(y)/out(y))
			new_rank[node] += d * (prev_rank[incoming_node] / out_degree[incoming_node])

		rank_sum += new_rank[node]


	print("rank_sum = ",rank_sum)
	return new_rank

# Create an object of Graph 
g = graph.generate_graph(total_nodes, total_edges)
ranks = [1.0 / total_nodes] * total_nodes
print("inital ranks =  ", ranks)

for iteration_numer in range(0, total_nodes, 1):
	ranks = calc_page_rank(ranks, g.in_link_nodes, g.out_degree)
	print("Page ranks = ", ranks)