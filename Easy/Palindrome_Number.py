class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            arr = [int(i) for i in str(x)]
            sub_array = arr[::-1]
            if arr == sub_array:
                return True
            else:
                return False
