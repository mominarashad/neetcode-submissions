class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash=[-1]*256

        left=0

        max_len=0

        for right in range(len(s)):

            if hash[ord(s[right])]!=-1:
                if hash[ord(s[right])]>=left:
                    left=hash[ord(s[right])]+1

            length=right-left+1
            max_len=max(max_len,length)
            hash[ord(s[right])]=right
        return max_len
        