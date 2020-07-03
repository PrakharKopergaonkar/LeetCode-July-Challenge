#Question 3 : Prison cells After N Days
class Solution:
    def nextDay(self, cells):
        temp_cells = cells.copy()
        for i in range(1,len(cells)-1):
            if(cells[i-1] == cells[i+1]):
                temp_cells[i] = '1'
            else:
                temp_cells[i] = '0'
        
        return temp_cells
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        blocksize = 0
        hashset = list()
        temp_string = ''.join(str(i) for i in cells)
        while(temp_string not in hashset):
            blocksize +=1
            hashset.append(temp_string)
            temp_list = [i for i in temp_string]
            temp_string = ''.join(i for i in self.nextDay(temp_list))
            if(blocksize==1):
                temp_string = '0' + temp_string[1:len(temp_string)-1]+'0'
        
        if(N<blocksize):
            return([int(i) for i in hashset[N]])
        else:
            m = N%blocksize
            index = hashset.index(temp_string)
            return [int(i) for i in hashset[index+(N-index)%(blocksize-index)]]
 