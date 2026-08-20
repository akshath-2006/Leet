class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s=[]
        cur=''
        for c in path+'/':
            if c=="/":
                if cur =="..":
                    if s:s.pop()

                elif cur!="" and cur!=".":
                    s.append(cur)
                cur=""
            else:   
                cur+=c
        return "/"+"/".join(s)