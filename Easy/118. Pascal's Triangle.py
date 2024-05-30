from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        pascal = [[1], [1,1]]
        
        for i in range(2, numRows):
            row = [1]*(i + 1)
            prev_row = pascal[-1]
            for j in range(1, len(prev_row)):
                row[j] = prev_row[j] + prev_row[j - 1]
            pascal.append(row)
        return pascal
            
print(Solution().generate(7))