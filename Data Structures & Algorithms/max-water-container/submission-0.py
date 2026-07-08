class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0

        low=0
        high=len(heights)-1

        while low <= high :
            width=high-low
            length=min(heights[low],heights[high])
            max_water=max(max_water,width*length)

            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1

        return max_water