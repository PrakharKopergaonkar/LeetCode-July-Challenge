# 3sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_set = []
        nums.sort()
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left = i+1
            right = len(nums)-1
            while(left<right):
                summation = nums[i]+nums[left]+nums[right]
                if(left!=i+1 and right!=len(nums)-1 and nums[left]==nums[left-1] and nums[right]==nums[right+1]):
                    left+=1
                    right-=1
                elif(summation>0):
                    right-=1
                elif(summation<0):
                    left+=1
                else:
                    solution_set.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    
            
        return solution_set
                    