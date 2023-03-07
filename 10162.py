n = int(input())

sec = [300,60,10]

count = []

for i in sec :
  m = n // i
  n -= m * i
  count.append(m)
  

if n != 0 :
  print(-1)
else :
  for i in range(len(count)) :
    print(count[i],end=" ")