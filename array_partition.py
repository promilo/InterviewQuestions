class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ind = 0
        output = 0
        while ind < len(nums):
            output += min(nums[ind], nums[ind + 1])
            ind += 2
        return output
