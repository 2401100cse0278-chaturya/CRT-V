'''
Double Linked List:
Dats store Node
Node 3 parts
1.Previous
2.Data
3.Next

Algorithm:
1.Create Node.
2.Insert the data into the node.
3.Generate the connection between the nodes.
4.Traverse all the nodes.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None 
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2 
node2.prev=node1
node2.next=node3
node3.prev=node2 
node3.next=node4
node4.prev=node3

def traverse():
    curr=node1
    while curr:
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
traverse()

def reverse_traverse():
    curr=node4
    while curr:
        print(curr.data,end=" <- ")
        curr=curr.prev
    print("None")
reverse_traverse()

#insertion at the beginning
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head

    if head:
        head.prev=new_node

    return new_node

#insertion at end
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr
    return head

#insertion after
def insertion_after(node,data):
    if node is None:
        print("Error")
        return
    new_node=Node(data)
    new_node.prev=node
    new_node.next=node.next
    if node.next:
        node.next.prev=new_node
    node.next=new_node

#inserion before
def insertion_before(node,data):
    if node is None:
        print("Error")
        return
    new_node=Node(data)
    new_node.next=node
    new_node.prev=node.prev
    if node.prev:
        node.prev.next=new_node
    node.prev=new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,30)
head=insert_begin(head,40)

print("Insertion at the begin")
traverse(head)

head=insert_end(head,50)
print("Insertion at the end")
traverse(head)

insertion_after(head.next,25)
print("Insertion after 30")
traverse(head)

insertion_before(head.next,20)
print("Insertion before 30")
traverse(head)