from bisect import bisect_left
from functools import cache

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance))
        walls.sort()

        @cache
        def dfs(i, j):
            if i < 0:
                return 0

            x, d = arr[i]

            left = x - d
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)

            l = bisect_left(walls, left)
            r = bisect_left(walls, x + 1)

            ans = dfs(i - 1, 0) + r - l

            right = x + d

            if i + 1 < n:
                if j == 0:
                    right = min(
                        right,
                        arr[i + 1][0] - arr[i + 1][1] - 1
                    )
                else:
                    right = min(
                        right,
                        arr[i + 1][0] - 1
                    )

            l = bisect_left(walls, x)
            r = bisect_left(walls, right + 1)

            ans = max(
                ans,
                dfs(i - 1, 1) + r - l
            )

            return ans

        return dfs(n - 1, 1)