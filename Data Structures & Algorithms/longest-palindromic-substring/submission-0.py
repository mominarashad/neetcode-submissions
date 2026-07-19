class Solution:
    def longestPalindrome(self, s: str) -> str:

        text2=s[::-1]
        n=len(s)
        m=len(text2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j]=0
        best_len=0
        best_end=0
        for i in range(1,n+1):
            for j in range(1,m+1):

                if s[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    length=dp[i][j]

                    if i-length==n-j:  #to check palindrome
                        if length > best_len:
                            best_len = length
                            best_end = i
                else:
                    dp[i][j]=0
                    
        return s[best_end - best_len : best_end]

        
        
        