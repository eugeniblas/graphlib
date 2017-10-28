from graph import Graph
def bfs(G, origen, destino):    
    
    visitados = []
    frontera = [(origen,[])]
    nodeActual = origen
    
    while (frontera) and (nodeActual != destino):
        nodeActual,pathActual = frontera.pop()
        if not(nodeActual in visitados):
            visitados.append(nodeActual)
            if (nodeActual != destino):
                visitados.append(nodeActual)
                for x in G.neighbors(nodeActual):
                    frontera.append((x,pathActual+[nodeActual]))
                    
    pathActual = pathActual + [nodeActual]
    return {
        'path' : pathActual,
        'expanded' : len(visitados)
    }