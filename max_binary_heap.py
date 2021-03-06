class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        

class MaxBinaryHeap:

    def __init__(self):
        self.values = []
        self.length = 0
    
    def enqueue(self, val):
        newNode = Node(val)
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
        max = self.values.pop()
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




this = MaxBinaryHeap()
this.enqueue(18)
this.print()
this.enqueue(27)
this.print()
this.enqueue(12)

this.print()
this.enqueue(33)
this.print()
this.enqueue(39)


this.print()
this.enqueue(55)
this.print()
this.enqueue(41)
this.print()
this.dequeue()
this.print()
this.dequeue()
this.print()
this.dequeue()
this.print()
this.dequeue()
this.print()
this.dequeue()
this.print()
this.dequeue()
this.print()

