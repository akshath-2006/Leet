class Solution(object):
    def maxAlternatingSum(self, nums):
        for i,v in enumerate(nums):
            nums[i]=v**2
        nums.sort()
        first=sum(nums[:len(nums)//2])
        last=sum(nums[len(nums)//2:])

        return last-first