def climbStairs(n):
  """
  Args:
      n : Integer

  Returns:
      fib[n]: Returns an int for the possible ways to climb the n-step.
  """
  fib = {}
  fib[1] = 1
  fib [2] = 2
  for i in range(3,n+1):
      fib[i] = fib[i-1] + fib[i-2]
  return fib[n]
