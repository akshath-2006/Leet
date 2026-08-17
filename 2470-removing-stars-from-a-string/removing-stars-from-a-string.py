class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s :
            if stack and i=="*":
                stack.pop()
                continue 
            stack.append(i)
        print(stack)
        return "".join(stack)
        