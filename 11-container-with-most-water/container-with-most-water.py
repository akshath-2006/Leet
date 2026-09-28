class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        res=0
        while l<r:
            area=(r-l)*min(height[r],height[l])
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            res=max(res,area)
        return res

