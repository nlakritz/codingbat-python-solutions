def combo_string(a, b):
  if len(a) < len(b):
    small = a
    big = b
  else:
    small = b
    big = a
  return small+big+small
