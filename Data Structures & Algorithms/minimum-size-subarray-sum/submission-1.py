class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        left=0
        min_len=float("inf")

        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                length=right-left+1
                min_len=min(min_len,length)
                sum-=nums[left]
                left+=1

        return min_len if min_len!= float('inf') else 0
        