def not_string(str):
  notString = "not"
  if (str.find("not") == 0): #returns starting index of search string if located, otherwise returns -1
    return str
  else:
    return "not " + str
