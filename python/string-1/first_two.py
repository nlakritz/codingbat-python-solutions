def first_two(str):
  end = 2
  if str < 2:
    end = len(str)
  return str[:end]
