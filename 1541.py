array =input().split('-')

res = int(array[0])
 
for i in range(1,len(array)) :
    res -= int(eval(array[i]))

print(res)