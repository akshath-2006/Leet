class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower() if i.isalpha() else i
        print(res)
        return res==res[::-1] 
        