class Solution:
    def decodeString(self, s: str) -> str:

        numsStack=[]
        strStack=[]

        curr=""
        num=0

        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)

            elif ch=='[':
                numsStack.append(num)
                strStack.append(curr)
                curr=""
                num=0
            elif ch ==']':
                k=numsStack.pop()
                val=strStack.pop()

                curr=val+curr*k
            else:
                curr+=ch
        return curr

        