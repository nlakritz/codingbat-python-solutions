def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a[len(b)*-1:] == b or b[len(a)*-1:] == a:
    return True
  return False
