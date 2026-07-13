class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        res=[]

        def solve(index,current):

            if index==n:
                return res.append(current[:])

            current.append(nums[index])
            solve(index+1,current)
            current.pop()
            solve(index+1,current)

            return res
        
        return solve(0,[])
        