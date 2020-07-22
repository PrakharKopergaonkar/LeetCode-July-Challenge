class Solution:
    def dfs(self,board,word,i,j,letter_count,visited):
        if(i>=len(board) or j>=len(board[0]) or i<0 or j<0) : return False
        elif([i,j] in visited) : return False
        elif(word[letter_count-1]!=board[i][j]): return False
        elif(letter_count==len(word) and board[i][j]==word[letter_count-1]):
            return True
        visited_temp = visited.copy()
        visited_temp.append([i,j])
        return self.dfs(board,word,i+1,j,letter_count+1,visited_temp) or self.dfs(board,word,i-1,j,letter_count+1,visited_temp) or self.dfs(board,word,i,j+1,letter_count+1,visited_temp) or self.dfs(board,word,i,j-1,letter_count+1,visited_temp)
            
        
            
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j]==word[0] and self.dfs(board,word,i,j,1,[])):
                    return True
        
        return False