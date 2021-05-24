def lone_sum(a, b, c):
  subtract = 0
  if a == b or a == c:
    subtract += a
  if b == a or b == c:
    subtract += b
  if c == a or c == b:
    subtract += c
  sum = a+b+c
  return sum - subtract
