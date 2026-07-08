class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n=len(s)
        hash=[0]*26
        left=0
        max_freq=0
        max_window=0
        for right in range(n):

            hash[ord(s[right])-ord('A')]+=1

            max_freq=max(max_freq,hash[ord(s[right])-ord('A')])
            window_size=right-left+1

            if window_size-max_freq>k:
                hash[ord(s[left])-ord('A')]-=1
                left+=1
            window_size=right-left+1
            max_window=max(max_window,window_size)

        return max_window



        