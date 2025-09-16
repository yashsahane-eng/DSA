class Solution(object):
    import math
    def uniquePaths(self, m, n):
        total_steps = m + n - 2
        steps_to_choose = min(m - 1, n - 1)
    
        result = 1
        for i in range(1, steps_to_choose + 1):
            result = result * (total_steps - steps_to_choose + i) // i
    
        return result
    