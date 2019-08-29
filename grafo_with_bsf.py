class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def show(self):
        for i in self.grafo:
            for j in i:
                print(j, end=" ")
            print("")

    def tem_ligacao(self, u, v):
        return self.grafo[u - 1][v - 1] == 1

    def bfs(self, v):
        #lista de visitados
        visitados = [False] * self.vertices
        # marce v como visitado
        visitados[v - 1] = True
        fila = [v - 1]
        print("%d visitado" % (v))
        while len(fila) > 0:
            #obtem o elemento da fila
            v = fila[0]
            #para ada vertice u adajacente a v
            for u in range(self.vertices):
                #verifica se tem conexao
                if self.grafo[v][u] == 1:
                    #verific se u nao foi visitado
                    if visitados[u] == False:
                        visitados[u] = True
                        fila.append(u)
                        print("%d visitado" % (u+1))
            fila.pop(0)

g = Grafo(10)
g.add_aresta(1, 4)
g.add_aresta(1, 3)
g.add_aresta(1, 2)
g.add_aresta(2, 5)
g.add_aresta(3, 6)
g.add_aresta(3, 7)
g.add_aresta(4, 8)
g.add_aresta(5, 9)
g.add_aresta(6, 10)

g.bfs(1)
