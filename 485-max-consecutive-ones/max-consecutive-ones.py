class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        m=0
        for i in nums:
            if i==1:
                count+=1
                m=max(count,m)
            if i==0:
                count=0
        return m
        