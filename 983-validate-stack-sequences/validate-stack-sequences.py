class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j=popped[::-1]
        stack=[]
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1]==j[-1]:
                stack.pop()
                j.pop()
                #j+=1
            
        return len(stack)==0

        