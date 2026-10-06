class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[0]*2*len(nums)
        for i in range((len(nums))):
            l[i]=nums[i] 
            l[i+len(nums)]=nums[i]

        return l