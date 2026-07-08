class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq={}

        for i,ch in enumerate(nums):
            diff=target-ch

            if diff in freq:
                return [freq[diff],i]

            freq[ch]=i

            