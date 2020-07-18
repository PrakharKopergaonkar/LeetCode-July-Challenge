#Question : Course Schedule II
class Solution:
    def dfs(self,at,schedule,pre_dict,visited):
        visited[at] = 1
        if(at in pre_dict) : 
            for i in pre_dict[at]:
                if(visited[i]==1) : return True
                if(visited[i]==0 and self.dfs(i,schedule,pre_dict,visited)): return True
        
        visited[at] = 2
        schedule.append(at)
        return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_dict = dict()
        for node in prerequisites:
            if(node[0] in pre_dict):
                pre_dict[node[0]].append(node[1])
            else:
                pre_dict[node[0]] = [node[1]]
        visited = [0]*numCourses
        schedule = []
        for at in range(0,numCourses):
            if(visited[at]==0 and self.dfs(at,schedule,pre_dict,visited)):
                return []
            
        return schedule