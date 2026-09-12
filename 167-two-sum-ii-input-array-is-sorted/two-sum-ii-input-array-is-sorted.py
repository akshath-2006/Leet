class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while l<r:
            cur=numbers[l]+numbers[r]
            if cur>target:
                r-=1
            elif cur<target:
                l+=1
            else:
                return [l+1,r+1]

        
