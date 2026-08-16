class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in s:
            if st and st[-1].lower()==i.lower() and st[-1]!=i:
                st.pop()
                continue
            st.append(i)
        res=''
        if st:
            for i in st:
                res+=i
        return res

