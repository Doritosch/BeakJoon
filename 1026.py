n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum  = 0

a.sort(reverse=True)

index = []

for i in range(n) :
  min = 100
  for j in range(n) : 
    if j in index : #b의 최솟값 index를 사용
      continue
    else : 
      if min >= b[j] :
        min = b[j]
        c= j  #index 저장
  index.append(c) #배열에 index 추가 
  sum += a[i] * min
print(sum)