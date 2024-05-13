class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    # First, reverse the matrix rows (flip the matrix vertically)
        matrix.reverse()
    
    # Now, transpose the matrix (swap rows with columns)
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):  # Note: Starting from `i+1` to avoid redundant swaps
            # Swap matrix[i][j] and matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        