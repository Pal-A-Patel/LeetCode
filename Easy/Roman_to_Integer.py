class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':   1000}
        pairs = zip(s[:-1], s[1:])
        return sum((-1 if Roman[a] < Roman[b] else 1)*Roman[a] for a, b in pairs) + Roman[s[-1]]
