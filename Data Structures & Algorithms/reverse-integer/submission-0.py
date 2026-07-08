class Solution:
    def reverse(self, x: int) -> int:
        
        is_neg=False

        if x<0:
            is_neg=True

        num=abs(x)

        res=0
        
        while num>0:
            digit=num%10
            res=res*10+digit
            num=num//10

        result = -res if is_neg else res

        if result >= -2**31 and result<2**31:
            return result
        else:
            return 0

