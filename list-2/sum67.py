def sum67(nums):
  sum = 0
  flag = False
  
  for num in nums:
    if num == 6:
      flag = True
    if not flag:
      sum += num
    if num == 7:
      flag = False
    
  return sum