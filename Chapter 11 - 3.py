n = int(input())
coin = list(map(int,input().split()))

least = 1
sum = 0
coin.sort()

print(coin)
li = []

for i in coin :
  li.append(i)
  sum += i
  
  least += 1
 
print(least)