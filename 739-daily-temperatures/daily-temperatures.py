class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s=[]
        answer=[0]*len(temperatures)
        
        for i,t in enumerate(temperatures):
            while s and t>s[-1][0]:
                val,ind=s.pop()
                answer[ind]=i-ind
            s.append([t,i])
        return answer

            













        # answer=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     j=i
        #     while(j<len(temperatures)):
        #         if(temperatures[i]<temperatures[j]):
        #             answer[i]=j-i
        #             break
        #         j+=1
        # return answer
                    



