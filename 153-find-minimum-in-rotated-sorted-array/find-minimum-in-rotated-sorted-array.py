class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=sorted(nums)
        while l!=nums:
            rem=nums.pop()
            nums.insert(0,rem)
        return nums[0]
