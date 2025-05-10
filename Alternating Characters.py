p='AAAA'
q=''
s=0
for y in range(len(p)-1):
    for x in range(len(p)-1):
        if p[x]==p[x+1]:
            q=q+p[x+1]
            s=s+1
        print(q)
print(s)
