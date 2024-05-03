def singleNumber(self, nums):
  """
  Args:
      nums: an Integer List

  Returns:
      int: Return elements that appear only once
  """
  dic = {}
  for num in nums:
      if num in dic:
          dic.pop(num)
      else:
          dic[num] = 1
  for k,v in dic.items():
      return k
