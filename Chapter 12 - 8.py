n = input()
sum = 0
li = list(n)

#���� ���� 
for i in range((len(n))) :
  for j in range((len(n))-i-1) :
    if ord(li[j]) >  ord(li[j+1]) :
      temp = li[j]
      li[j] = li[j+1]
      li[j+1] = temp

for i in range(len(li)) :
  if ord(li[i]) < 58 :  #�ƽ�Ű �ڵ� ���� ���� ���� ���� 
    sum += int(li[i])
  else :  #���ڸ� 
    del li[0:i]
    break 

li.append(sum)  #����Ʈ �ڿ� �� ����

st = ''.join(map(str,li)) #����Ʈ -> ���ڿ�, int���� str���� ���� ���ڿ��� �Ϸ��� map�� �����

print(st)