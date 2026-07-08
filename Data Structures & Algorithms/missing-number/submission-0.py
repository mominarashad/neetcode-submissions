class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        requiredSum=n*(n+1)//2
        sum=0
        for ch in nums:
            sum+=ch

        return requiredSum-sum