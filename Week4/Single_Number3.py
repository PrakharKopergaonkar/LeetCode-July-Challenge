#Question 3 : Single Number 3

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x_or = 0
        output_list = [0]*2
        for i in range(0,len(nums)):
            x_or = x_or ^ nums[i]
        bitflag = x_or & ~ ((x_or - 1))
        
        for i in nums:
            if(i & bitflag ==0):
                output_list[0] ^= i
            else:
                output_list[1] ^= i
        
        return output_list
                