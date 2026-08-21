class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op="+-*/"
        s=[]
        for v in tokens:
            if v in op:
                b=s.pop()
                a=s.pop()
                if v=="+":
                    s.append(a+b)
                    continue
                elif v=="-":
                    s.append(a-b)
                    continue
                elif v=="/":
                    s.append(a // b if a * b >= 0 else -(abs(a) // abs(b)))
                    continue
                elif v=="*":
                    s.append(a*b)
                    continue
            s.append(int(v))
        return s[0]

        