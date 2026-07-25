class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.rtype = []

        if len(nums) > 1:
            for num1 in range(len(nums)):
                for num2 in range(len(nums)):
                    if (nums[num1] + nums[num2]) == target and num1 != num2:
                        self.rtype = [num2, num1]
                        break

        return self.rtype