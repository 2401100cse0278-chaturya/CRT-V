class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Double_LL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            return new_node
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
        return self.head

    def deletion_begin(self):
        if self.head is None:
            print("Empty")
            return None 
        new_head=self.head
        self.head=self.head.next 
        del new_head

    def deletion_end(self):
        if self.head is None:
            print("Empty")
            return None
        if self.head.next is None:
            self.head=None 
            return 
        curr=self.head
        while curr.next:
            curr=curr.next 
        curr.prev.next=None 
        curr.prev=None

    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        count=0
        curr=self.head
        while curr:
            count +=1
            curr=curr.next
        return count 
    def delete_at_position(self,pos):
        if pos<0 and pos>self.count_nodes():
            print("Error")
            return
        if pos==0:
            return self.deletion_begin()
        if pos==(self.count_nodes()-1):
            return self.deletion_end()
        curr=self.head 
        for i in range(pos):
            curr=curr.next 
        curr.prev.next=curr.next 
        curr.next.prev=curr.prev
        del curr
    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next

        print("None")
dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)
dll.traverse()
dll.insert_end(40)
dll.insert_end(50)
dll.traverse()
dll.deletion_begin()
dll.traverse()
dll.deletion_end()
dll.traverse()
print(dll.count_nodes())
dll.delete_at_position(2)
dll.traverse()