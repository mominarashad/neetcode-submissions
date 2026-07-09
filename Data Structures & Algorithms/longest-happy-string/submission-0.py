class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap=[]
        res=[]
        if a>0:
            heapq.heappush(max_heap,(-a,'a'))
        
        if b>0:
             heapq.heappush(max_heap,(-b,'b'))
        if c>0:
             heapq.heappush(max_heap,(-c,'c'))

        while max_heap:

            curr_count,curr_char=heapq.heappop(max_heap)
            curr_count=-curr_count

            if len(res)>=2 and res[-1]==curr_char and res[-2]==curr_char:
                if not max_heap:
                    break
                
                next_count,next_char=heapq.heappop(max_heap)
                next_count=-next_count

                res.append(next_char)
                next_count-=1

                if next_count>0:
                    heapq.heappush(max_heap,(-next_count,next_char))
                
                heapq.heappush(max_heap,(-curr_count,curr_char))
            
            else:
                res.append(curr_char)
                curr_count-=1
                if curr_count>0:
                    heapq.heappush(max_heap,(-curr_count,curr_char))

        return "".join(res)

                

                

        