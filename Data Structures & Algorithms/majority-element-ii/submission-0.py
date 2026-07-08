class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        res=[]
        for val,count in freq.items():
            if count>(n/3):
                res.append(val)
        return res

        