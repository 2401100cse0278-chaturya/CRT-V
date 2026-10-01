class Circular_Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.q=[None]*self.size
    def enqueue(self,val):
        # check Queue is full 
        if self.front==(self.rear+1)%self.size:
            return "Queue is full"
        #Queue is empty
        if self.front==-1:
            self.front=0
        self.rear = (self.rear+1)%self.size 
        self.q[self.rear]=val 
    def dequeue(self):
        if self.front==-1:
            return "Queue is empty"
        val=self.q[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size 
        return val 
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.q[i], end=" -> ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
cq = Circular_Queue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.display()

    
#Leetcode:
#20. Valid Parentheses
def isValid(self, s: str) -> bool:
    stack=[]
    map={")":"(","}":"{","]":"["}
    for char in s:
        if char in map:
            top_ele=stack.pop() if stack else "#"
            if map[char]!=top_ele:
                return False
        else:
            stack.append(char)
    return not stack

#232:Implement Queue using Stacks

def __init__(self):
    self.stack1=[]
    self.stack2=[]

def push(self, x: int) -> None:
    self.stack1.append(x)
    
def pop(self) -> int:
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    return self.stack2.pop()
    
def peek(self) -> int:
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    return self.stack2[-1]
def empty(self)->bool:
    return len(self.stack1)==0 and len(self.stack2)==0

    
