class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charcount = {}
        for i in s:
            if i in charcount.keys():
                charcount[i] += 1
            else:
                charcount[i] = 1

        odd = 0
        for i in charcount.keys():
            if charcount[i] % 2 == 1:
                odd += 1

        if odd > 1:
            return False
        else:
            return True
