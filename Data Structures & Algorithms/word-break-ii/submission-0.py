class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set=set(wordDict)
        n=len(s)

        
        
        def solve(index):
            if index==n:
                return [""]
            res=[]

            for i in range(index,n):
                word=s[index:i+1] 
                if word in word_set:
                    remaining_words=solve(i+1)
                    for sen in remaining_words:
                        if sen =="":
                            res.append(word)
                        else:
                            res.append(word+" "+sen)

            return res
        return solve(0)
        