def dfs(visited, stack, graph, node):
    visited.append(node)
    stack.append(node)
    while stack:
        s = stack.pop()
        print(s, "is removed")

        for adjacent in graph[s]:
            if adjacent not in visited:
                visited.append(adjacent)
                stack.append(adjacent)
    
    print(visited)
    
    
def input_graph(graph):
    
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node == 'done':
            break

        adjacent_nodes_input = input(f"Enter adjacent nodes for '{node}' (comma-separated): ")
        if adjacent_nodes_input.strip() == "":
            graph[node] = []
        else:
            adjacent_nodes = adjacent_nodes_input.split(',')
            graph[node] = [adj.strip() for adj in adjacent_nodes]

    print("Graph:", graph)
    
    return graph
    
def main():
    graph = {}
    graph = input_graph(graph)
    visited = []
    stack = []
    dfs(visited, stack, graph, 'a')

main()
