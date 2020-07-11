#Question : Subsets : Given a set of distinct integers, nums, return all possible subsets (the power set).

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        if(len(nums)==0) : return subsets
        
        def generate_subsets(nums,position,list1):
            subsets.append(list1)
            for i in range(position,len(nums)):
                generate_subsets(nums,i+1,list1+[nums[i]])
        generate_subsets(nums,0,[])
        return subsets