import math

count = 0
prime_list = []
for num in range(2,20,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        prime_list.append(num)
        count+=1

print(count)
print(len(prime_list))
