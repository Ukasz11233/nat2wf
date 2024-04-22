import re

def parse_mermaid_edges(mermaid_graph):
    edges = []
    lines = mermaid_graph.replace(" ", "").split('\n')
    for line in lines:
        edge = []
        if(line and line[0].isupper()):
            edge.append(line[0])
            index = line.find(">")
            if(index > 0 and index < len(line)):
                edge.append(line[index+1])
        if(len(edge) == 2):
            edges.append(edge)
    return edges


def has_cycle(graph_edges):
    visited = set()
    graph = {}

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False
    

    for edge in graph_edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False

mermaid_graph = """
graph TD
    A(Start: Open drawer)
    B{Is item blue pen?}
    C(Take out item)
    D{Is item blue pen?}

    A --> B
    B -- No --> C
    C --> D
    D -- Yes --> F(End: Blue pen found)
    D -- No --> C
"""

mermaid_graph2 = """
A[Start] –> B[Enter year]
B -> C[Is the year divisible by 4?]
C – Yes –> D[Is the year divisible by 100?]
C – No –> E[Is the year divisible by 400?]
D – Yes –> F[Is the year divisible by 400?]
D – No –> G[Is the year divisible by 400?]
E – Yes –> H[Leap Year]
E – No –> I[Not a Leap Year]
F – Yes –> H
F – No –> I
G – Yes –> H
G – No –> I
H[Terminate]
I[Terminate]
"""


mermaid_graph3_without_loop = """
A[Turn on the computer]
B[Enter username and password to log in]

C[Open desired software or application]

 D[Perform required tasks]

E[Save any changes made]

F[Shut down the computer]
A –> B;
B –> C;
C –> D;
D –> E;
E –> F;
"""

def print_all_edges(graph_edges):
    for edge in graph_edges:
        print(f"{edge[0]} --> {edge[1]}")


graph_edges = parse_mermaid_edges(mermaid_graph3_without_loop)
print_all_edges(graph_edges)
print(graph_edges)




if has_cycle(graph_edges):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")

