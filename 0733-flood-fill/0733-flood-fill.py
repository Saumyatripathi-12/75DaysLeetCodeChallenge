from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        # If color is already same
        if original == color:
            return image

        def dfs(r, c):
            # Boundary check and color match
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != original
            ):
                return

            # Fill color
            image[r][c] = color

            # Visit 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image