def rotate(self, nums, k):
  """
  Args:
      nums[List[int]] : integer array
      k[int] : rotate the array to the right by k steps
  """
  k %= len(nums)
  nums[:] = nums[-k:] + nums[:-k]
