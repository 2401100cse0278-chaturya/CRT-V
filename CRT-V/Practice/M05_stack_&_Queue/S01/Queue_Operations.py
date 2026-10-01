'''
class queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,val):
        self.q.append(val) 
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q.pop(0)
    def is_empty(self):
            return len(self.q)==0
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q[0]
    def size(self):
        return len(self.q)
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.is_empty())
print(q.peek())
print(q.dequeue())
print(q.size())
'''
