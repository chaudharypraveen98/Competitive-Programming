def dijkstra_algorithm(graph, start, end):
    unseen_nodes = graph
    shortest_path={}
    inf = float("inf")
    predecessor ={}

    for node in unseen_nodes:
        shortest_path[node]=inf
    shortest_path[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_path[node]<shortest_path[min_node]:
                min_node = node
        
        for child_node,weight in shortest_path[min_node].items():
            if weight+ shortest_path[min_node]<shortest_path[child_node]:
                shortest_path[child_node] = shortest_path+weight
                predecessor[child_node] = min_node

        unseen_nodes.pop(min_node)
    
    path = []
    current_node = end
    while current_node!= start:
        try:
            path.insert(0,current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('path not reachable')
    path.insert(0, start)

    if shortest_path[end]!=inf:
        print(shortest_path[end])
        print(path)


# 0 3 2 0 0
# 3 0 5 3 0
# 2 5 0 0 20
# 0 3 0 0 4
# 0 0 20 4 0
# 0 4

def construct_graph(n):
    graph={}
    for i in range(n):
        

test_cases = int(input())
no_of_vertix = int(input())
