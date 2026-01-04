#two sum - leetcode
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(len(nums)):
            for y in range(x+1,len(num)):
                if(nums[x]+nums[y]]==targrt):
                    return([x,y])
        
