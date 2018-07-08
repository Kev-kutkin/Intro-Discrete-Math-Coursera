import networkx as nx


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    
    # Write your code here.
    w = 0
    cycle.append(cycle[0])
    for i in range(len(cycle)-1):
    #print(cycle1[i], cycle1[i+1])
        w += sum(g[cycle[i]][cycle[i+1]].values())
    return w

