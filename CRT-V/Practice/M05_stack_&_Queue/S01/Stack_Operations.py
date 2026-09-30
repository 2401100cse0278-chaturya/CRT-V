# Implementation of a stack using list

class stack:
    def __init__(self):
        self.s = []
    def push(self,val):
        self.s.append(val)
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.s.pop()
    def is_empty(self):
        return len(self.s)==0
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[-1]
    def size(self):
        return len(self.s)
st=stack()
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.peek())
st.pop()
print(st.size())

# Stack implemetation using variables

class StackWithTop:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.s=[None]*self.size
    def push(self,val):
        if self.top==self.size - 1:
            return "stack is full"
        self.top+=1
        self.s[self.top]=1
    def is_empty(self):
        return self.top==-1
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        val=self.s[self.top]
        self.pop=-1
        return val 
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[self.top]
    def size(self):
        return self.top+1
st=StackWithTop(5)
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.peek())
print(st.pop())
print(st.peek())

# Stack implementation using single linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return "Stack is empty"
        val = self.top.data
        self.top = self.top.next
        return val
    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data
    def display(self):
        temp=self.top 
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next 
        print()
st1=Stack_LL()
st1.push(100)
st1.push(200)
st1.push(500)
st1.display()
print(st1.peek())
print(st1.pop())
st1.display()