class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         bottom=0
         top=len(matrix)-1
         valid_row=-1
         while bottom<= top:
            valid_mid = (top+bottom)//2
            if matrix[valid_mid][0]<=target<= matrix[valid_mid][-1]:
                valid_row = valid_mid
                break
            elif matrix[valid_mid][0]<target:
                bottom+=1
            else:
                top-=1
         if valid_row==-1:
                return False    
             
         row=matrix[valid_row] 
         left=0
         right=len(row)-1
         while left<=right:
                mid = (left+right)//2
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    left+=1
                else:
                    right-=1
         return False                   
