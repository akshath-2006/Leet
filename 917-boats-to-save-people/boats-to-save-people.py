class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        l,r=0,len(people)-1
        people.sort()
        tog=0
        while l<r:
            if people[l]+people[r]>limit:
                r-=1
            elif people[l]+people[r]<=limit:
                print(people[l],people[r])
                tog+=1
                l+=1
                r-=1
            # elif people[l]+people[r]==limit:
            #     tog+=1
            #     r-=1
            #     l+=1
            # else:
            #     l+=1
            #     r-=1
        return tog+(len(people)-2*tog)

