class Solution:

    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n

        k %= total

        result = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                new_flat = (r * n + c + k) % total

                new_r = new_flat // n
                new_c = new_flat % n

                result[new_r][new_c] = grid[r][c]

        return result