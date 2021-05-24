def lucky_sum(a, b, c):
  list = [a, b, c]
  sum = 0
  for item in list:
    if item == 13:
      break;
    sum += item
  return sum
