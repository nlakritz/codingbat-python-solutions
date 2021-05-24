def make_bricks(small, big, goal):
  closestFive = int(goal/5) * 5
  if closestFive > big * 5:
    closestFive = big * 5
  if goal <= closestFive + small:
    return True
  return False