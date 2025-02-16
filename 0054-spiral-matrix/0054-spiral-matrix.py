from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans = []

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1  # Move top boundary down

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1  # Move right boundary left

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1  # Move left boundary right

        return ans
