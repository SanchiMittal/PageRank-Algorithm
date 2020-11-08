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

	Returns:
	list of ranks(size: iterations+1)
	list of rank_sums(size: iterations+1)
	"""
	ranks = [0]*(iterations + 1)
	rank_sums = [0]*(iterations + 1)
	ranks[0] = init_rank
	for i in range(1, iterations + 1, 1):
		ranks[i], rank_sums[i] = calc_page_rank(ranks[i - 1], in_link_nodes, out_degree, d, total_nodes, total_edges)
	
	return ranks, rank_sums


def get_whole_ranks(ranks):
	"""
	Args: array of ranks from a single iteration
	Returns: array of whole no. ranks
	"""
	whole_ranks = {}
	sorted_ranks = sorted(ranks)
	for i in range(len(ranks)):
		whole_ranks[i] = sorted_ranks.index(ranks[i])+1

	return whole_ranks
