#question 4: ugly numbers II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = list()
        ugly_numbers.append(1)
        i, j, k = 0, 0, 0
        while(len(ugly_numbers)<n):
            two = ugly_numbers[i]*2
            three = ugly_numbers[j]*3
            five = ugly_numbers[k]*5
            minimum = min(two,three,five)
            if(minimum not in ugly_numbers):
                ugly_numbers.append(minimum)
            if(minimum==two):
                i+=1
            elif(minimum == three):
                j+=1
            else:
                k+=1
        
        return(ugly_numbers[len(ugly_numbers)-1])