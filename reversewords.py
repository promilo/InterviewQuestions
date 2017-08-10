class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        splited = s.split(" ")
        for i, x in enumerate(splited):
            if i == (len(splited) - 1):
                output += x[::-1]
            else:
                output += x[::-1]
                output += " "
        return output
