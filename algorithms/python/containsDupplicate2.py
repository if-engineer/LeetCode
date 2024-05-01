def containsNearbyDuplicate(self, nums, k):
  """

  Args:
      nums (int): an Integer List
      k (int): an Integer

  Returns:
      bool : True -> duppicate, False -> not dupplicate
  """
  d = {}
  for i, num in enumerate(nums):
      if num in d and abs(d[num] - i) <= k:
          return True
      else:
          d[num] = i
  return False
