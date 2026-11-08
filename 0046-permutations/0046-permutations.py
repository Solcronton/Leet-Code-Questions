class Solution:
    def permute(self, nums):
        ans = []
        temp = []
        visited = [False] * len(nums)

        def solve():
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return

            for i in range(len(nums)):
                if not visited[i]:
                    temp.append(nums[i])
                    visited[i] = True

                    solve()

                    # Backtracking
                    temp.pop()
                    visited[i] = False

        solve()
        return ans