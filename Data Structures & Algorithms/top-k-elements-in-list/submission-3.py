class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1

        buckets=[[] for _ in range(len(nums)+1)]

        for num, f in freq.items():
            buckets[f].append(num)

        result=[]

        for i in range(len(buckets)-1,-1,-1):

            for num in buckets[i]:

                result.append(num)

                if len(result)==k:
                    return result