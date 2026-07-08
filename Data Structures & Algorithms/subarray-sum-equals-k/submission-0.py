class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix=0
        counter=0
        seen=defaultdict(int)
        seen[0]=1

        for i in range(len(nums)):
            prefix+=nums[i]
            counter+=seen[prefix-k]
            seen[prefix]+=1

        return counter
