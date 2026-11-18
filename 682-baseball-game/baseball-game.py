class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for i in operations :
            if i.lstrip("-").isdigit():
                stack.append(int(i))
                continue
            elif i=="+":
                a=stack.pop()
                s=a+stack[-1]
                stack.append(a)
                stack.append(s)
            elif i=="C":
                stack.pop()
            elif i=="D":
                stack.append(stack[-1]*2)
        print(stack)
        return sum(stack)