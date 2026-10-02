class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c=""
        for ch in range(len(min(strs,key=len))):
            for j in strs:
                if strs[0][ch]!=j[ch]:
                    return c
            c+=strs[0][ch]
        return c 

        