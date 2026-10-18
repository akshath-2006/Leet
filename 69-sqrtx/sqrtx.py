class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=1
        g=0
        while a<x:
            if g>x:
                return (a-1)//1
            a+=1
            g=a*a
        if not x:
            return 0
        return 1