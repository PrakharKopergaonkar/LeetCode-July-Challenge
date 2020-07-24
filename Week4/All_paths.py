#Question 24: All Paths From Source to Target
class Solution:
    def dfs(self,curr_position,graph,all_paths,visited):
        if(curr_position==len(graph)-1):
            all_paths.append(visited)
            return 
        for node in graph[curr_position]:
            self.dfs(node,graph,all_paths,visited+[node])
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        all_paths = []
        self.dfs(source,graph,all_paths,[0])
        return all_paths
    