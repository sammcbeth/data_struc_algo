class WeightedGraph:

    def __init__(self):
        self.edgeList = {}

    def addVertex(self, vertex):
        try:
            self.edgeList[vertex]
        except:
            self.edgeList[vertex] = []
        
    def addEdge(self, vertex1, vertex2, weight):
        self.edgeList[vertex1].append({'node':vertex2,'weight':weight})
        self.edgeList[vertex2].append({'node':vertex1,'weight':weight})


this = WeightedGraph()
this.addVertex('a')
this.addVertex('b')
this.addVertex('c')
this.addVertex('d')
this.addEdge('a','b',9)
this.addEdge('a','c',5)
this.addEdge('b','c',7)
print(this.edgeList)