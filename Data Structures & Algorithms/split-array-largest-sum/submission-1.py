class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def count_subarrays(max_sum):
            subarray=1
            load=0

            for num in nums:
                if (load+num)>max_sum:
                    subarray+=1
                    load=0
                
                load+=num

            return subarray<=k

        low=max(nums)
        high=sum(nums)

        while low<high:
            mid=(low+high)//2

            if count_subarrays(mid):
                high=mid
            else:
                low=mid+1

        return low
        