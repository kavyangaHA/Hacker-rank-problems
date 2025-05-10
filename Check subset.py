#import time
#t1=time.time()
num_of_test_cases=int(input())
for x in range(num_of_test_cases):
    num_of_elements_in_A=int(input())
    A=str(input())
    A=A.split(' ')
    A=set(A)
    num_of_elements_in_B=int(input())
    B=str(input())
    B=B.split(' ' )
    B=set(B)
    if A & B==A:
        print(True)
    else:
        print(False)
#t2=time.time()
#print('Total time=',t2-t1)
