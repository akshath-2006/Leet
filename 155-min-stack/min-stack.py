class MinStack(object):

    def __init__(self):
        self.s=[]
        self.m=[99999999999999999]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value <=self.m[-1]:
            self.m.append(value)
        self.s.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.s[-1]==self.m[-1]:
            self.m.pop()
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()