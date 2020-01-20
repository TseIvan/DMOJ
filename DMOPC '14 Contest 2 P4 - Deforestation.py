# Faster input to avoid TLE instead of using input()
from sys import stdin, stdout
total = int(stdin.readline())
pfx = [0] * (total+2)

for i in range(1,total+1):
  pfx[i] = pfx[i-1] + int(stdin.readline())
for i in range(int(stdin.readline())):
  i = list(map(int,stdin.readline().split()))
  print(pfx[int(i[1]) + 1] - pfx[int(i[0])])
