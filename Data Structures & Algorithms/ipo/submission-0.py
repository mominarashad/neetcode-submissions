class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        sorted_res=sorted(zip(capital,profits))
        
        max_heap=[]

        idx=0

        while k>0:
            k-=1

            while idx<n and sorted_res[idx][0]<=w:
                heapq.heappush(max_heap,-sorted_res[idx][1])
                idx+=1

            if not max_heap:
                break

            w+=-heapq.heappop(max_heap)

        return w



            


        