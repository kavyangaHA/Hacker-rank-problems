MyList=["apple","banana","grapes","papaya"]
print(MyList[-1])
MyList.insert(1,"orange")
print(MyList)

MyList.pop()
print(MyList)

del MyList[0]
print(MyList)

#MyList.clear()
#print(MyList)

for x in MyList:
    print(x)
print()

for i  in range(len(MyList)):
    print(MyList[i])
print()

i=0
while i <len(MyList):
    print(MyList[i])
    i=i+1

print()
t=[print(x) for x in MyList]
print(t)

print()
t=[x for x in MyList]
print(t)

MyList=["apple","banana","grapes","papaya"]
newList=[x for x in MyList if x!="apple"]

mew2=[x for x in range(1,10)]
mew3=[x for x in range(1,10)if (x<5) and (x!=2)]

MyList.sort()
print(MyList)
#case sensitive sorting
MyList=["apple","Banana","grapes","Papaya"]
MyList.sort(key=str.lower) #okkom wacha tik lower krl sort krnw
print(MyList)
print()
MyList.sort(reverse=True)
print(MyList)

print()

def myFunc(n):
    return abs(n-50)
list2=[100,200,30,40,50]
list2.sort(key=myFunc)
print(list2)


thislist = ["banana", "Orange", "Kiwi", "cherry"]#Case sensitive sorting can give an unexpected result:
thislist.sort()
print(thislist)

list3=list2.copy() #copy-method1
print(list2)
list2[1]=1000
print(list3[1])

list3=list(list2)#copying-method 2
list4=list2[:]#copying method 3
