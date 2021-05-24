def string_splosion(str):
  count = 1
  newStr = ""
  while count <= len(str):
    newStr += str[:count]
    count += 1
  return newStr
