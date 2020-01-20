# The first line will contain the number T (1≤T≤10) which is the number of different tests that will be run. Each test has the form of an integer N (1≤N≤100000) on the first line of the test, followed by a list of the N cars listed from top to bottom. The cars will always use the numbers from 1 to N in some order.
out = []
for test in range(int(input())):
  cars = [int(input()) for _ in range(int(input()))]

  branch = []
  start = 1
  success = False
  while(True):
    if len(cars) > 0: # Amount remaining on mountain
      if cars[-1] == start: # Matches on mountain dequeue
        cars.pop()
        start += 1
      elif (len(branch) > 0 and branch[-1] == start): # Branch Match
        branch.pop()
        start += 1
      else: # No match on branch or mountain dump into branch
        branch.append(cars.pop())
    elif (len(branch) > 0):
      if branch[-1] == start:
        branch.pop()
        start += 1
      else:
        break
    else: # Branch and Mountain len == 0
      success = True
      break
  x = out.append("Y") if success else out.append("N")
[print(_) for _ in out]
