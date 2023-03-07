n = input()

sorted_n = sorted(n,reverse= True)

answer = int("".join(sorted_n))

if (answer % 10 != 0) | (answer % 3 != 0) :
  print(-1)
else :
  print(answer)