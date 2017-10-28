from graph import Graph
def dfs(G, origen, destino, depth=0):
    
    visitados = []
    frontera = [(origen,[])]
    nodeActual = origen
    
    while (frontera) and (nodeActual != destino):
        nodeActual,pathActual = frontera.pop([0])
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