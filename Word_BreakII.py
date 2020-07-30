class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False]*len(s)
        output_list = collections.defaultdict(list)
        # output_list[0] = [""]
        #word break 1 logic
        for i in range(0,len(s)):
            if(s[0:i+1] in wordDict):
                dp[i] = True
            else:    
                for j in range(i,0, -1):
                    if(s[j:i+1] in wordDict and dp[j-1]):
                        dp[i] = True
                        break
        
        if(not dp[-1]):
            return []
        
        
        for i in range(0,len(s)):
            if(not dp[i]) : continue
            for j in range(i,-1,-1):
                if(j==0 and s[j:i+1] in wordDict):
                    output_list[i].append(s[j:i+1])
                elif(j>0 and s[j:i+1] in wordDict and dp[j-1]):
                    for word in output_list[j-1]:
                        output_list[i].append(word + " " + s[j:i+1])
        return(output_list[len(s)-1])
                