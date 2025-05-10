###A1=str(input())
##A='1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78'
##A=A.split(' ')
###A=list(map(int,A))
###print(A)
##A=set(A)
##B='1 2 3 4 5 50'
##B=B.split(' ')
###B=list(map(int,A))
##B=set(B)
##if B & A==B and B!=A:
##    print('True')
##else:
##    print('False')


A=str(input())
A=A.split(' ')
A=list(map(int,A))
A=set(A)
n=int(input())
t=0
for x in range(n):
    B=str(input())
    B=B.split(' ')
    B=list(map(int,B))
    B=set(B)
    if A & B ==B and A!=B:
        t=t+1
if t==n:
    print('True')
else:
    print('False')
