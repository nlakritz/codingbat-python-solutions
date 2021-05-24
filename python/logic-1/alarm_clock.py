def alarm_clock(day, vacation):
  weekend = False
  if day == 0 or day == 6:
    weekend = True
  if (vacation and not weekend) or (not vacation and weekend):
    return "10:00"
  elif (vacation and weekend):
    return "off"
  else:
    return "7:00"