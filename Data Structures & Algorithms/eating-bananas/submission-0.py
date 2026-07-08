class Solution:
    from typing import List
    import math

    def findMax(self,piles):
        n=len(piles)
        maxi=float('-inf')

        for i in range(n):
            maxi=max(maxi,piles[i])
        return maxi
    def findHours(self,piles,h):
        n=len(piles)
        totalHours=0

        for i in range(n):
            totalHours +=math.ceil(piles[i]/h)
        return totalHours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=self.findMax(piles)

        while(low<=high):
            mid=(low+high)//2

            totalH=self.findHours(piles,mid)

            if totalH<=h:
                high=mid-1
            else:
                low=mid+1
        return low

        