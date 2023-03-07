n = int(input())

km = list(map(int,input().split()))
oil = list(map(int,input().split()))

price = 0

for i in range(n-1) :
  price += km[i] * oil[i]
  if oil[i] < oil[i+1] :
    oil[i+1] = oil[i]

print(price)