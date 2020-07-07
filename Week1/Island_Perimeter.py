#Question 7: Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        if(len(grid)==0) : return 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    side_included = 0
                    if(i==0 or grid[i-1][j]==0):
                        side_included+=1
                    if(i==len(grid)-1 or grid[i+1][j]==0):
                        side_included+=1
                    
                    if(j==0 or grid[i][j-1]==0):
                        side_included+=1
                    
                    if(j==len(grid[0])-1 or grid[i][j+1]==0):
                        side_included+=1
                
                    perimeter+=side_included
        
        return perimeter