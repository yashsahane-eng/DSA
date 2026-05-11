import sys

sys.stdin = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\input.txt', 'r')
sys.stdout = open(r'C:\Users\sahan\Desktop\Python-DSA\python code\output.txt', 'w')

class Solution:

    def sumoffirstlastelement(self, nums):

        if not nums:
            return 0

        first = nums[0]
        last = nums[-1]

        return first + last


solution = Solution()

nums = list(map(int, input().split()))

ans = solution.sumoffirstlastelement(nums)

print(ans)