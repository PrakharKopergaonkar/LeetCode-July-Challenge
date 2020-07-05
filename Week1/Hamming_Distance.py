#Question 5:Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        if(len(a)<len(b)):
            a='0'*(len(b)-len(a))+a
        elif(len(a)>len(b)):
            b='0'*(len(a)-len(b))+b
        changes = 0
        for i in range(0,len(a)):
            if(a[i]!=b[i]):
                changes+=1
        
        return changes