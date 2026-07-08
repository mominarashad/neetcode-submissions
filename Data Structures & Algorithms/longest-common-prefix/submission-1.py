class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first=strs[0]
        second=strs[-1]
        res=[]
        for i in range(len(first)):
            if first[i]!=second[i]:
                break
            res.append(first[i])
        return "".join(res)
