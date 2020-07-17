import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums)==0) : return output_list
        dictonary = dict()
        for i in range(0,len(nums)):
            if(nums[i] in dictonary):
                dictonary[nums[i]] += 1
            else:
                dictonary[nums[i]] = 1
        heap = [(key, value) for key, value in dictonary.items()]
        heapq.heapify(heap)
        maximum = heapq.nlargest(k,heap,key=lambda x : x[1])
        return [i[0] for i in maximum]
        
        
        