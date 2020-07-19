#Question : Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(len(a)>len(b)):
            b = '0'*(len(a)-len(b)) + b
        elif(len(b)>len(a)):
            a = '0'*(len(b)-len(a)) + a
        
        carry = '0'
        summation = ''
        length = len(b)-1
        while(length>=0):
            count_one = 0
            if(a[length]=='1'):
                count_one+=1
            if(b[length]=='1'):
                count_one+=1
            if(carry=='1'):
                count_one+=1
            curr = int(a[length]) ^ int(b[length]) ^ int(carry)
            if(count_one>1):
                carry = '1'
            else:
                carry = '0'
            summation = str(curr) + summation
            length-=1
        if(carry=='1'):
            summation = carry + summation
        return summation