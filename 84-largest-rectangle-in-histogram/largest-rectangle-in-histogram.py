class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right=[len(heights)]*len(heights)
        left=[-1]*len(heights)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else len(heights)
            stack.append(i)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        maxarea=0
        area=0
        print(right,left)
        for i,h in enumerate(heights):
            area=h*(right[i]-left[i]-1)
            maxarea=max(maxarea,area)
        return maxarea
