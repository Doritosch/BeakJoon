n = int(input())

sum = 0

array =[]

for i in range(n) :
  array.append(int(input()))

array.sort()

#병렬 연결
for i in range(n) :
  if sum < array[i] * (n-i) :
    sum = array[i] * (n-i)

print(sum)