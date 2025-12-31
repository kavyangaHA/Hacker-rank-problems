print("##Stack")
stack=[1,2,3,4,5]

#methods = push(),pop(),isEmpty(),peek(),size()

#push()
stack.append(16)
print(stack)

#pop()
p=stack.pop()
print("pop element = ",p)

#peek
topElement=stack[-1]
print("peek = ",topElement)

#isEmpty
isEmpty =not bool(stack)
print("isEmpty:",isEmpty)

#size
print("Size: ",len(stack))

print()
print("##Queue")
#Queue
#enqueue() ,dequeue(),peek(),isEmpy,size()

queue=[]

#Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue =",queue)

#Dequeue
element =queue.pop(0)
print("Dequque: ",element)

#Peek
frontElement =queue[0]
print("Peek: ",frontElement)

#isEmpty
isEmpty=not bool(queue)
print("isEmpty: ",isEmpty)

#SiZE
print("Size: ",len(queue))
