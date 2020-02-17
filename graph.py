

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

    def DFS(self, vertex):
        results = []
        visited = {}
        def DFS_helper(vertex,results,visited):
            # print(results)
            if not self.edgeList[vertex]:
                return None
            results.append(vertex)
            visited[vertex] = True
            for val in self.edgeList[vertex]:
                if val not in visited:
                    results,visited = DFS_helper(val,results,visited)
            return results,visited
        return DFS_helper(vertex,results,visited)[0]

    def DFS_iterative(self, vertex):
        s = []
        s.append(vertex)
        visited = {}
        result = []
        while len(s) > 0:
            vertex = s.pop()
            if vertex not in visited:
                result.append(vertex)
                visited[vertex] = True
            for val in self.edgeList[vertex]:
                if val not in visited:
                    s.append(val)
        return result
    
    def BFS(self, vertex):
        queue = [vertex]
        results = []
        visited = {}
        currentVertex = None

        while(len(queue)):
            currentVertex = queue.pop(0)
            results.append(currentVertex)
            visited[currentVertex] = True

            for val in self.edgeList[currentVertex]:
                if val not in visited:
                    visited[val] = True
                    queue.append(val)
        return results



        

    
    def print(self):
        print(self.edgeList)


this = Graph()
# this.addVertex('Dallas')
# this.addVertex('Tokyo')
# this.addVertex('San Francisco')
# this.addVertex('New York')
# this.addVertex('Chicago')
# this.addVertex('Atlanta')
# this.addVertex('Tampa')
# this.addEdge('Dallas','Tokyo')
# this.addEdge('New York','Tokyo')
# this.addEdge('Dallas','San Francisco')
# this.addEdge('Chicago','San Francisco')
# this.addEdge('Atlanta','Chicago')
# this.addEdge('Tampa','San Francisco')
# this.addEdge('New York','San Francisco')
# this.addEdge('Dallas','Atlanta')
this.addVertex('A')
this.addVertex('B')
this.addVertex('C')
this.addVertex('D')
this.addVertex('E')
this.addVertex('F')

this.addEdge('A','B')
this.addEdge('A','C')
this.addEdge('B','D')
this.addEdge('C','E')
this.addEdge('D','E')
this.addEdge('D','F')
this.addEdge('E','F')

# this.removeVertex('San Francisco')
print(this.BFS('A'))
print(this.DFS('A'))
print(this.DFS_iterative('A'))
# this.print()