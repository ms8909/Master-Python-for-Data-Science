n = 9
for a in range(1, n+1):
  a = a - (n//2 +1)
  if a < 0:
    a = -a
  print(" " * a + "*" * (n - a*2) + " "*a)