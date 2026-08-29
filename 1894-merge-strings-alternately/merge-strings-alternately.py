class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=""
        w1,w2=len(word1)-1,len(word2)-1
        a,b=0,0
        for i in range(len(word1)+len(word2)):
            if a<=w1:
                res+=word1[a]
                a+=1
            if b<=w2:
                res+=word2[b]
                b+=1
            
        return res
            
            