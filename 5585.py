#�ʹ� ���̽� ���� ���ߴ�.
n = int(input())

#coin = [500,100,50,10,5,1] �ְ� for �� ������ ���ݾ�

ex = 1000 - n

count = 0

while(True) :
  if(ex // 500 > 0) :
    count += 1 *(ex // 500)
    ex = ex - ((ex // 500) * 500)
  if(ex // 100 > 0) :
    count += 1 *(ex // 100)
    ex = ex - ((ex // 100) * 100)
  if(ex // 50 > 0) :
    count += 1 *(ex // 50)
    ex = ex - ((ex // 50) * 50)
  if(ex // 10 > 0) :
    count += 1 *(ex // 10)
    ex = ex - ((ex // 10) * 10)
  if(ex // 5 > 0) :
    count += 1 *(ex // 5)
    ex = ex - ((ex // 5) * 5)
  if(ex // 1 > 0) :
    count += 1 *(ex // 1)
    ex = ex - ((ex // 1) * 1)
  if ex == 0 :
    break

#�ʹ� ���ݾ�

print(count)