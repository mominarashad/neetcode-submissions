class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        
        s1_hash=[0]*26
        s2_hash=[0]*26
        if m>n:
            return False

        for i in range(m):
            s1_hash[ord(s1[i])-ord('a')]+=1
            s2_hash[ord(s2[i])-ord('a')]+=1

        if s1_hash==s2_hash:
            return True

        for i in range(m,n):
            s2_hash[ord(s2[i])-ord('a')]+=1
            s2_hash[ord(s2[i-m])-ord('a')]-=1

            if s1_hash==s2_hash:
               return True
        return False



        