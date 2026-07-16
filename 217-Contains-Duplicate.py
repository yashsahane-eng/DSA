class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)

        cd=set()

        for i in range(n):
            if nums[i] in cd:
                return True
            
            cd.add(nums[i])
        return False