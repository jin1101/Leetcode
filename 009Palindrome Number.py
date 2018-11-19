class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            reversed_int = int(str(x)[::-1])
            if x == reversed_int:
                return True
            return False