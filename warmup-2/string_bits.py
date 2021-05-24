def string_bits(str):
  i = 0;
  newStr = ""
  while i < len(str):
    newStr += str[i]
    i += 2
  return newStr
