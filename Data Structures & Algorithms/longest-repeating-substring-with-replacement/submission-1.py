class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hash=[0]*26
        left=0
        n=len(s)

        max_window=0
        max_freq=0
        for right in range(n):
            hash[ord(s[right])-ord('A')]+=1

            max_freq=max(max_freq,hash[ord(s[right])-ord('A')])
            window=right-left+1

            if window-max_freq>k:
                hash[ord(s[left])-ord('A')]-=1
                left+=1

            window=right-left+1
            max_window=max(max_window,window)

        return max_window

        


            
            