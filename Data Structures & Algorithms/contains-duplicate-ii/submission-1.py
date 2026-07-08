class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()

        n=len(nums)
        i=0
        for j in range(n):

            if j-i>k:
                window.remove(nums[i])
                i+=1

            if nums[j] in window:
                return True
            window.add(nums[j])
            
        return False


        