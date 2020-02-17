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
    
    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        for val in self.edgeList:
            if val == start:
                distances[val] = 0
                nodes.enqueue(val, 0)
            else:
                distances[val] = 99999999999
                nodes.enqueue(val, 99999999999)
            previous[val] = None
        while len(nodes):
            smallest = nodes.dequeue().val
            if smallest == finish:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                break
            if smallest or distances[smallest] != 99999999999:
                for neighbor in self.edgeList[smallest]:
                    # print(distances)
                    # print(previous)
                    nodes.print()
                    candidate = distances[smallest] + neighbor['weight']
                    if candidate < distances[neighbor['node']]:
                        distances[neighbor['node']] = candidate
                        previous[neighbor['node']] = smallest
                        nodes.enqueue(neighbor['node'], candidate)
        return path[::-1]




class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        

class PriorityQueue:

    def __init__(self):
        self.values = []
        self.length = 0
    
    def enqueue(self, val, priority):
        newNode = Node(val, priority)
        if self.length == 0:
            self.values.append(newNode)
            self.length += 1
            return self
        self.values.append(newNode)
        self.length += 1
        n = self.length -1
       
        while n > 0:
            if self.values[n].val < self.values[(n-1)//2].val:
                self.values[n].val, self.values[(n-1)//2].val = self.values[(n-1)//2].val,self.values[n].val
                n = (n-1)//2
            else:
                return self

    def print(self):
        arr = []
        for val in self.values:
            arr.append(val.val)
        print(arr)

    def dequeue(self):
        n = 0
        self.values[n].val, self.values[self.length - 1].val = self.values[self.length - 1].val, self.values[n].val
        min = self.values.pop()
        self.length -= 1
        
        def sinkDown():
            n = 0
            while 2*n + 1 < self.length:
                
                if 2*n + 2 == self.length:
                    if self.values[n].val > self.values[2*n + 1].val:
                        self.values[n].val, self.values[2*n + 1].val = self.values[2*n + 1].val,self.values[n].val
                        return self
                    else:
                        return self
                elif self.values[2*n + 1].val > self.values[2*n + 2].val:
                    if self.values[n].val > self.values[2*n + 2].val:
                        self.values[n].val, self.values[2*n + 2].val = self.values[2*n + 2].val,self.values[n].val
                        n = 2*n + 2
                else:
                    if self.values[n].val > self.values[2*n + 1].val:
                        self.values[n].val, self.values[2*n + 1].val = self.values[2*n + 1].val,self.values[n].val
                        n = 2*n + 1
                    else:
                        return self
        sinkDown()
        return min


    
    




this = WeightedGraph()
this.addVertex('A')
this.addVertex('B')
this.addVertex('C')
this.addVertex('D')
this.addVertex('E')
this.addVertex('F')
this.addEdge('A','B',4)
this.addEdge('A','C',2)
this.addEdge('B','E',3)
this.addEdge('C','D',2)
this.addEdge('C','F',4)
this.addEdge('D','E',3)
this.addEdge('D','F',1)
this.addEdge('E','F',1)
# print(this.edgeList)

print(this.Dijkstra('A', 'E'))