def missing_char(str, n):
  if (n == 0): # remove first char
    return str[1:] 
  elif (n == len(str)-1): # remove last char
    return str[:-1] 
  else:
    return str[:n] + str[n+1:] # remove some middle char
