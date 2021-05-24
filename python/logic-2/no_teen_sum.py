def no_teen_sum(a, b, c):
  list = [a, b, c]
  sum = 0
  for item in list:
    sum += fix_teen(item)
  return sum
  
def fix_teen(n):
  if n >= 13 and n <= 19 and n != 15 and n != 16:
    return 0
  return n
