class Solution:
    def partition(self, s: str) -> List[List[str]]:

            def check_palindrome(low,high):

                while low<=high:
                    if s[low]!=s[high]:
                        return False
                    
                    low+=1
                    high-=1

                return True

            n=len(s)
            res=[]
            def solve(index,current):

                if index==n:
                    return res.append(current[:])

                for i in range(index,n):
                    if check_palindrome(index,i):
                        current.append(s[index:i+1])
                        solve(i+1,current)
                        current.pop()

                return res

            return solve(0,[])
        