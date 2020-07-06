# Question 6: Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry = 1
        while(i>=0):
            if(carry==0):
                break
            else:
                digits[i]+=carry
                if(digits[i]==10):
                    digits[i] = 0
                    carry = 1
                else:
                    carry = 0
                if(i==0 and carry==1):
                    digits.insert(0,1)
                    carry = 0
            i-=1
        return digits
                    