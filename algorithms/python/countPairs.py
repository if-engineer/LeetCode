def countPairs(self, nums, target):
        """
        :type nums: List[int],
        :type target: int
        :return int
        """
        counter = 0
        left, right = 0, len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] < target:
                counter += right - left
                left += 1
            else:
                right -= 1
        return counter
