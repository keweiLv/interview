from functools import cache
from math import inf

from operator import le
import re
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left, right = i+1, n-1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_index = {}
        ans = inf
        for j,x in enumerate(nums):
            if x in last_index:
                ans = min(ans,j-last_index[x])
            rev = int(str(x)[::-1])
            last_index[rev] = j
        return ans if ans < inf else -1

    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))

    # 两栋颜色不同且距离最远的房子
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        c = colors[0]
        if c != colors[-1]:
            return n-1
        r = n -2
        while colors[r] == c:
            r -=1
        l = 1
        while colors[l] == c:
            l += 1
        return max(r,n-1-l)

    max = lambda a,b:b if b > a else a
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        @cache
        def dfs(i:int,j:int,k:int) -> int:
            if i < 0 or j < 0 or k < 0:
                return -inf
            if i == 0 and j == 0:
                return 0
            x = grid[i][j]
            if x > 0:
                k -= 1
            return max(dfs(i-1,j,k),dfs(i,j-1,k)) + x
        ans = dfs(len(grid) - 1,len(grid[0]) - 1,k)
        dfs.cache_clear
        return -1 if ans < 0 else ans


def main():
    nums = [12,21,45,33,54]
    sol = Solution()
    # res = sol.threeSum(nums)
    res = sol.minMirrorPairDistance(nums)
    print(res)


if __name__ == "__main__":
    main()
