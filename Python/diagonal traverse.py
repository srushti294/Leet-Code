class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return 0
        num_rows,num_cols=len(mat),len(mat[0])
        diagonals = [[] for _ in range(num_rows+num_cols-1)]
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i+j].append(mat[i][j])
        res = diagonals[0]
        for x in range(1,len(diagonals)):
            if (x%2==1):
                res.extend(diagonals[x])
            else:
                res.extend(diagonals[x][::-1])