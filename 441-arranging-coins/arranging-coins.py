class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=0,n
        res=0
        while l<=r:
            m=(l+r)//2
            slots=(m*(m+1))//2
            if  slots > n:
                r=m-1
            else :
                l=m+1
                res=max(m,res)
        return res
        