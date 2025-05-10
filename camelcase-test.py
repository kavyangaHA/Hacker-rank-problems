s='saveChangesInTheEditor'
m='oneTwoThree'
#Method 1

p=1
for x in s:
    if x==x.upper():
        p=p+1
print(p)

#Method-2
q=1
for x in m:
    if str(x)<'Z':
        q+=1
print(q)
