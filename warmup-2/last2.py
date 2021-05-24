def last2(str):
  substring = str[-2:]
  count = 0
  for i in range(len(str)-2):
    if ((str[i] == substring[0]) and (str[i+1] == substring[1])):
      count += 1
  return count