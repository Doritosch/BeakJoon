#1������ ����
#������ ��ȣ ������ �ٽ� 1��
#1�� �԰� ���� ��ȣ
#food_times = ������ ��� �Դµ� �ʿ��� �ð� =
#k�� �Ŀ� �ٽ� �Ծ���� ��ȣ

def solution(food_times, k):
    answer = 0
    #��ȣ
    num = 0
    
    while True :
      if k == 0 :
        answer = num  #k�� �� �Ծ�� �� ���� ��ȣ
        return answer 
      if food_times[num] != 0 : #������ �� ���� �ʾ��� ��
        food_times[num] -= 1
        k -= 1  #1�� ���
      num = (num + 1) % len(food_times) #��ȣ ��ȸ ##����Ʈ ���� len()
      
  
food_times = list(map(int,input().split()))
k = int(input())

print(solution(food_times, k))

