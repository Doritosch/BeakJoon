n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum  = 0

a.sort(reverse=True)

index = []

for i in range(n) :
  min = 100
  for j in range(n) :
    if j in index :
      continue
    else :
      if min >= b[j] :
        min = b[j]
        c= j
  index.append(c)
  sum += a[i] * min
print(sum)