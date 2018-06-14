def Count(N):
  sumup = 0
  for value in N:
    if value == 1:
      sumup += 1
      if sumup > 5:
        return "#coderlifematters"
      elif value == 0:
        sumup = 0
        continue
  return "#allcodersarefun"
x = Count([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(x)
