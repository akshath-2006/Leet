class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in asteroids:
            collided=False
            while s and s[-1]*i<0 and i<0:
                if abs(i)>abs(s[-1]):
                    s.pop()
                elif abs(i)<abs(s[-1]):
                    collided=True
                    break
                else:
                    s.pop()
                    collided=True
                    break
            if not collided:
                s.append(i)
        return s