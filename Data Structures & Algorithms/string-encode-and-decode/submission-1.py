class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for ch in strs:
            encoded+=str(len(ch))+'#'+ch
        return encoded

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1

            length=int(s[i:j])
            start=j+1

            words=s[start:start+length]
            res.append(words)
            i=start+length
        return res

