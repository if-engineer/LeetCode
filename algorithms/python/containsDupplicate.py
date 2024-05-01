def containsDuplicate(self, nums):
  """_summary_

  Args:
      nums (int): an Integer Array
  Returns:
      bool : True -> duppicate, False -> not dupplicate
  """
  return len(set(nums)) != len(nums)
