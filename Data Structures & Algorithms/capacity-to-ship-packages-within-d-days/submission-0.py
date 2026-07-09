class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def find_days(capacity):

            d=1
            load=0

            for w in weights:

                if (load+w)>capacity:
                    d+=1
                    load=0

                load+=w

            return d<=days

        low=max(weights)
        high=sum(weights)

        while low <high:
            mid=(low+high)//2

            if find_days(mid):
                high=mid
            else:
                low=mid+1
        return low
        