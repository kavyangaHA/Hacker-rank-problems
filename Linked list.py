# Without __str__ method
class Dog:
    def __init__(self,name):
        self.name=name
d=Dog("rexy")
print(d)#Without __str__ method we get the address of the object("rexy")
        #not the value


# With __str__ method
class Dog:
    def __init__(self,name):
        self.name=name
    def __str__(dog):
        return f"Dog named {dog.name}"
d=Dog("rexy")
print(d)#With __str__ method we get the value of the object
        #we don't get the adress 

#Singly Linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(3)
print(node1)#when we create the class we do not use the __str__ method
            #so without it when we print the node1 we get the address
            #not the value
print(node1.data)
print(node1.next)
        
node2=Node(6)
print(node2.data)
print(node2.next)

node3=Node(9)
print(node3.data)
print(node3.next)

node4=Node(12)
print(node4.data)
print(node4.next)
                
print()

node1.next=node2 #now node1.next means the address of the node2
node2.next=node3
node3.next=node4

print(node2)
print(node1.next)
print("Above are same")
print("....")

currentNode=node1 #currentNode means the address to the node1
print(currentNode)

while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode=currentNode.next
print("null")

#doubly linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
node1=Node(3)
node2=Node(5)
node3=Node(15)       
node4=Node(20)

node1.next=node2

node2.prev=node1
node2.next=node3

node3.prev=node2
node3.next=node4

node4.prev=node3


print("\nTraversing forward:")

currentNode=node1

while currentNode:
    print(currentNode.data,end=" -> ")
    currentNode = currentNode.next

print("null")

print("\nTraversing backward:")
currentNode =node4
while currentNode:
    print(currentNode.data,end=" -> ")
    currentNode=currentNode.prev
print("null")

print()
#Circular Doubly Linked List Implementation

print("###Circular Doubly Linked List Implementation")

node1.prev=node4
node4.next=node1
print("\nTraversing forward:")
currentNode =node1
startNode=node1

print(currentNode.data, end=" -> ")
currentNode =currentNode.next

while currentNode !=startNode:
    print(currentNode.data,end=" -> ")
    currentNode=currentNode.next
print("........")



print("\nTraversing backward:")
currentNode =node4
startNode=node4

print(currentNode.data, end=" -> ")
currentNode =currentNode.prev

while currentNode !=startNode:
    print(currentNode.data,end=" -> ")
    currentNode=currentNode.prev
print("........")

























