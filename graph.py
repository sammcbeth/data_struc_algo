

class Graph:

    def __init__(self):
        self.edgeList = {}
    
    def addVertex(self, name):
        try:
            if self.edgeList[name]:
                return None
        except:
            self.edgeList[name] = []
            return self
    
    def addEdge(self, vertex1, vertex2):
        self.edgeList[vertex1].append(vertex2)
        self.edgeList[vertex2].append(vertex1)
    
    def removeEdge(self, vertex1, vertex2):
        self.edgeList[vertex1].remove(vertex2)
        self.edgeList[vertex2].remove(vertex1)
    
    def removeVertex(self, vertex):
        remove_arr = self.edgeList[vertex]
        self.edgeList.pop(vertex)
        for key in remove_arr:
            if vertex in self.edgeList[key]:
                self.edgeList[key].remove(vertex)

    
    def print(self):
        print(self.edgeList)


this = Graph()
this.addVertex('Dallas')
this.addVertex('Tokyo')
this.addVertex('San Francisco')
this.addVertex('New York')
this.addEdge('Dallas','Tokyo')
this.addEdge('New York','Tokyo')
this.addEdge('Dallas','San Francisco')
this.removeVertex('San Francisco')
this.print()