class Solution:
    def trap(self, height: List[int]) -> int:

        low=0
        high=len(height)-1

        left_max=0
        right_max=0

        water=0

        while low < high:

            if height[low]<height[high]:
                left_max=max(left_max,height[low])
                water+=left_max-height[low]
                low+=1
            else:
                right_max=max(right_max,height[high])
                water+=right_max-height[high]
                high-=1

        return water

        