def ijobiy_yigindi(*sonlar):
  yigindi = 0
  for son in sonlar:
    if son > 0:
      yigindi += son
  return yigindi