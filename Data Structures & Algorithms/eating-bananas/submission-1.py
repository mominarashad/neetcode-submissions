from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def find_hours(hour):
            total_hours=0

            for i in range(len(piles)):
                total_hours+=ceil(piles[i]/hour)
            return total_hours

        low=1
        high=max(piles)

        while low<=high:
            mid=(low+high)//2

            h_t=find_hours(mid)
            
            if h_t>h:
                low=mid+1
            else:
                high=mid-1

        return low

        