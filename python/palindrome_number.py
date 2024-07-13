class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x_invert = x[::-1]
        return x == x_invert