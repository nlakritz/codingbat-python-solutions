def close_far(a, b, c):
  count = 0;
  count += abs(a-b) + abs(a-c) + abs(b-c)
  if count == 4 and (a != b != c):
    return False
  return True
