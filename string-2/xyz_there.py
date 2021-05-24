def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3] == "xyz":
      if str[i-1] != "." or i == 0:
        return True
  return False
