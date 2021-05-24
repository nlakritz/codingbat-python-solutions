def centered_average(nums):
  rawSum = 0
  for num in nums:
    rawSum += num

  max = nums[0]
  min = nums[0]
  for num in nums:
    if num > max:
      max = num
    if num < min:
      min = num
  
  adjustedSum = rawSum - max - min
  return adjustedSum/(len(nums)-2)