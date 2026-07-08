class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = set()
        if n < 4:
            return []

        for i in range(n - 3):
            for j in range(i + 1, n - 2):

                low = j + 1
                high = n - 1

                while low < high:
                    total = nums[i] + nums[j] + nums[low] + nums[high]

                    if total == target:
                        res.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                        high -= 1
                    elif total < target:
                        low += 1
                    else:
                        high -= 1

        return [list(quadruple) for quadruple in res]