class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash=[-1]*256

        n=len(s)

        left=0
        max_length=0
        for right in range(n):

            if hash[ord(s[right])]!=-1:
                if hash[ord(s[right])]>=left:
                    left=hash[ord(s[right])]+1

            length=right-left+1
            max_length=max(max_length,length)
            hash[ord(s[right])]=right

        return max_length

        