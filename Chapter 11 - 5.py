#n개의 볼링공 
#무게가 다른 것 고르기
n,s = map(int,input().split())
li = list(map(int,input().split()))

count = 0

for x in range(n) :
 for y in range(x+1,n) :
   if li[x] != li[y] :
     count += 1 
     
print(count)      