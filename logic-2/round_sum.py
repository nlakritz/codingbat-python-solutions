def round_sum(a, b, c):
  list = [a,b,c]
  sum = 0
  for num in list:
    sum += round10(num)
  return sum
  
def round10(num):
  if num % 10 >= 5:
    num += 10 - (num % 10)
  else:
    num -= num % 10
  return num
