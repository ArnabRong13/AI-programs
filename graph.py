def graph_input(graph):
    node = input("Enter a node:")
    graph[node] = []
    
    return graph

def create_graph():
    graph = {}
    while(1):
        choice = int(input("Enter your choice.\n1) Add node. \n2) Display. \n3) Exit."))
        if(choice == 1):
            graph = graph_input(graph)
        elif(choice == 2):
            print(graph)
        elif(choice == 3):
            return 0

create_graph()