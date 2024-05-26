class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, x in enumerate(nums):
            print(x)
            y = target - x
            if y in m:
                return [m[y], i]
            m[x] = i

          
