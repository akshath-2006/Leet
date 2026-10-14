class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(r+l)//2
            if matrix[m][-1] < target:
                l=m+1
            elif target < matrix[m][0]:
                r=m-1
            else:
                break
        #if not (l<=r):
            # return False
        res=matrix[m]
        l1=0
        r1=len(res)-1
        while l1<=r1:
            m1=(l1+r1)//2
            if target < res[m1]:
                r1=m1-1
            elif target > res[m1]:
                l1=m1+1
            else:
                return True
        return False