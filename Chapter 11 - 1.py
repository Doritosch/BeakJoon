import time
#
start_time = time.time(); #

n = input().split()

x = list(map(int,input().split()))
x.sort(reverse=True)

group = 0
data = 0

for i in x :
  if data == 0 : 
    data = i
    group += 1
  data -= 1
      
print(group)

end_time = time.time(); #
print("time : ",end_time - start_time) #