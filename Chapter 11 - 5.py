#n���� ������ 
#���԰� �ٸ� �� ����
n,s = map(int,input().split())
li = list(map(int,input().split()))

count = 0

for x in range(n) :
 for y in range(x+1,n) :
   if li[x] != li[y] :
     count += 1 
     
print(count)      