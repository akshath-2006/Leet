class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalpha():
                l+=1
            elif not s[r].isalpha():
                r-=1
            else:
                res[l],res[r]=res[r],res[l]
                l+=1
                r-=1
        return "".join(res)
