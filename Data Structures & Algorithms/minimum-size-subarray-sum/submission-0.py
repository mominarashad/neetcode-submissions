class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left=0
        min_length=float("inf")
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]

            while sum>=target:
                length=right-left+1
                min_length=min(min_length,length)
                sum-=nums[left]
                left+=1

        return min_length if min_length!=float("inf") else 0
 
        