n = (input())

length = int(len(n))

l = 0
r = 0

for i in range(length // 2) :
  l += int(n[i]) 
  r += int(n[i+(length // 2)])

if l == r :
  print("LUCKY")
else :
  print("READY")