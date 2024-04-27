def targetIndices(self, nums, target):
  """"
  Args:
        nums:List[int],
        target:int,
  Returns:
          List[int]
  """
  return [i for i, num in enumerate(sorted(nums)) if num == target]
