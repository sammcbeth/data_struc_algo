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
            if self.values[n].priority < self.values[(n-1)//2].priority:
                self.values[n].val, self.values[(n-1)//2].val = self.values[(n-1)//2].val,self.values[n].val
                self.values[n].priority, self.values[(n-1)//2].priority = self.values[(n-1)//2].priority,self.values[n].priority
                n = (n-1)//2
            else:
                return self

    def print(self):
        arr = []
        for val in self.values:
            arr.append([val.val, val.priority])
        print(arr)

    def dequeue(self):
        n = 0
        self.values[n].val, self.values[self.length - 1].val = self.values[self.length - 1].val, self.values[n].val
        self.values[n].priority, self.values[self.length - 1].priority = self.values[self.length - 1].priority, self.values[n].priority
        max = self.values.pop()
        self.length -= 1
        
        def bubbleUp():
            n = 0
            while 2*n + 1 < self.length:
                
                if 2*n + 2 == self.length:
                    if self.values[n].priority > self.values[2*n + 1].priority:
                        self.values[n].val, self.values[2*n + 1].val = self.values[2*n + 1].val,self.values[n].val
                        self.values[n].priority, self.values[2*n + 1].priority = self.values[2*n + 1].priority,self.values[n].priority
                        return self
                    else:
                        return self
                elif self.values[2*n + 1].priority > self.values[2*n + 2].priority:
                    if self.values[n].priority > self.values[2*n + 2].priority:
                        self.values[n].val, self.values[2*n + 2].val = self.values[2*n + 2].val,self.values[n].val
                        self.values[n].priority, self.values[2*n + 2].priority = self.values[2*n + 2].priority,self.values[n].priority
                        n = 2*n + 2
                else:
                    if self.values[n].priority > self.values[2*n + 1].priority:
                        self.values[n].val, self.values[2*n + 1].val = self.values[2*n + 1].val,self.values[n].val
                        self.values[n].priority, self.values[2*n + 1].priority = self.values[2*n + 1].priority,self.values[n].priority
                        n = 2*n + 1
                    else:
                        return self
        bubbleUp()
        return max




this = PriorityQueue()
this.enqueue('john',18)
this.print()
this.enqueue('amy',27)
this.print()
this.enqueue('sue',12)

this.print()
this.enqueue('beau',33)
this.print()
this.enqueue('william',39)


this.print()
this.enqueue('jeff',55)
this.print()
this.enqueue('max',41)
this.print()
print(this.dequeue().priority)
print(this.dequeue().priority)
print(this.dequeue().priority)
print(this.dequeue().priority)
print(this.dequeue().priority)
print(this.dequeue().priority)


# this.print()
# this.dequeue()
# this.print()
# this.dequeue()
# this.print()
# this.dequeue()
# this.print()
# this.dequeue()
# this.print()
# this.dequeue()
# this.print()

