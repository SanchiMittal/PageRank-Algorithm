def calc_page_rank(prev_rank, in_link_nodes, out_degree, d=0.85, total_nodes=10, total_edges=30):
	new_rank = [(1.0 - d) / total_nodes] * total_nodes
	rank_sum = 0.0

	# Calculate new rank for each node
	for node in range(0, total_nodes, 1):

		# iterate all incoming_node such that there's an edge incoming_node -> node
		for incoming_node in in_link_nodes[node]:
			# PR(x) = (1 - d)/N + d * (for each edge y -> x, PR(y)/out(y))
			new_rank[node] += d * (prev_rank[incoming_node] / out_degree[incoming_node])

		rank_sum += new_rank[node]


	# print("rank_sum = ",rank_sum)
	return new_rank, rank_sum



def get_all_ranks(init_rank, in_link_nodes, out_degree, d=0.85, total_nodes=10, total_edges=30, iterations=3):
	"""
	Args:
	init_rank -> array of initial ranks
	in_link_nodes -> list of no. of incoming links for all nodes
	out_degree -> list of no. of out degree for all nodes
	total_nodes -> total no. of nodes
	total_edges -> total no. of edges
	d -> damping factor
	total_iterations
	"""
	ranks = init_rank
	final_ranks = [0]*iterations
	rank_sums = [0]*iterations
	for i in range(0, iterations, 1):
		final_ranks[i], rank_sums[i] = calc_page_rank(ranks, in_link_nodes, out_degree, d, total_nodes, total_edges)
	
	return final_ranks, rank_sums