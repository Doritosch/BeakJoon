#shift + insert = paste

n = int(input())

array = []

count = 1

#2���� ����Ʈ
for i in range(n) :
  array.append(list(map(int,input().split())))

#���� if 4 4 / 4 4 / 1 4 = 1 4 / 4 4 / 4 4
array.sort(key=lambda x : x[0]) 
array.sort(key=lambda x : x[1])
#�ʱⰪ
temp = array[0]
#�� �ð��� ���� ù �ð� ��
for i in range(1,len(array)) :
  if temp[1] <= array[i][0] :
    temp = array[i]
    count+=1
    
print(count)