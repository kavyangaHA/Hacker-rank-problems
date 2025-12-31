nums=[0,0,1,1,1,2,2,3,3,4]
#nums=[0,0,0,0,0,0,0,0]
#nums=[1,1,2]
'''
l=[]
for x in range (len(nums)):
    if nums[x] not in l:
        l+=[nums[x]]
    else:
        nums.remove(nums[x])
        x=x-1
print(l)
print(nums)'''

l=[]
n=0
while n<len(nums):
    if (nums[n] in l):
        nums.remove(nums[n])
    else:
        l+=[nums[n]]
        n+=1
print(len(l))
print(l)
print(nums)
