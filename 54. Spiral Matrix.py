class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            #1
            ans += matrix.pop(0)
            #2
            if matrix and matrix[0]:
                for r in matrix:
                    ans.append(r.pop())
            #3 
            if matrix and matrix[-1]:
                ans += matrix.pop()[::-1]
            #4
            if matrix and matrix[-1]:
                for r in matrix[::-1]:
                    ans.append(r.pop(0))
        return ans