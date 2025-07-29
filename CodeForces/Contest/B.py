def min_coins(arr):
  """
  Finds the minimum number of coins needed to make an array non-decreasing.

  Args:
      arr: A list of integers representing the array.

  Returns:
      The minimum number of coins needed.
  """

  n = len(arr)
  dp = [0] * (n + 1)  # dp array to store minimum coins for subarrays

  # Iterate from i = 2 to i < n
  for i in range(2, n):
    prev_element = arr[i - 1]
    current_element = arr[i]

    # Check if previous element is less than or equal to current element
    if prev_element <= current_element:
      dp[i] = dp[i - 1]
    else:
      # Cost of increasing the current element
      cost = prev_element - current_element + 1
      dp[i] = min(dp[i], dp[i - 1] + cost)

  # Handle last element separately (no comparison needed)
  if n > 1 and arr[n - 1] > arr[n - 2]:
    dp[n] = dp[n - 1] + 1  # Cost of increasing the last element
  else:
    dp[n] = dp[n - 1]

  return dp[n]


# Test cases
test_cases = [
  [1, 7, 9],
  [2, 1, 4, 7, 6],
  [1, 3, 2, 4],
  [179],
  [344, 12, 37, 60, 311, 613, 365, 328, 675]
]

for arr in test_cases:
  coins = min_coins(arr)
  print(coins)
