def big_diff(nums):
  max = nums[0]
  min = nums[0]
  for num in nums:
    if num > max:
      max = num
    if num < min:
      min = num
  return max-min
