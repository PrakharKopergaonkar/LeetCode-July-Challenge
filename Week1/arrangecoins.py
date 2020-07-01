#Question 1 : Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = n
        i = 1
        if(n==1) : return 1
        if(n==0) : return 0
        while(a-i>=0):
            a-=i
            i+=1
        
        return i-1
