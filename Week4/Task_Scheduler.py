from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_list = []
        heapq.heapify(task_list)
        for k,v in Counter(tasks).items():
            heapq.heappush(task_list,(-v,k))
            
        
        max_number = heapq.heappop(task_list)
        counter = 1
        while(len(task_list)>0):
            number = heapq.heappop(task_list)
            if(number[0]==max_number[0]):
                counter+=1
            else:
                break
        res = (-max_number[0] - 1) * (n+1) + counter
        return max(res,len(tasks))
        