print("Start execution")

from pagerank_basic import graph
from pagerank_basic.pagerank import get_all_ranks, get_whole_ranks
total_nodes = 10 # total no. of nodes
total_edges = 30 # total no. of edges
d = 0.85 # damping factor
total_iterations = 3

# Create an object of Graph 
g = graph.generate_graph(total_nodes, total_edges)
ranks = [1.0 / total_nodes] * total_nodes
print("inital ranks =  ", ranks)

all_ranks, rank_sums = get_all_ranks(ranks, g.in_link_nodes, g.out_degree, d, total_nodes, total_edges, total_iterations)

for i in range(total_iterations+1):
    print("\nIteration", i, ":")
    print("Page ranks = ", all_ranks[i])
    print("Rank Sum = ", rank_sums[i])

final_ranks = get_whole_ranks(all_ranks[-1])
print("\nPage","\t", "Rank")
for page in final_ranks:
    rank = final_ranks[page]
    print(page, '\t', rank)


print("Program Terminated")