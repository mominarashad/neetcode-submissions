class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor=0
        for ch in nums:
            xor^=ch
        return xor
        