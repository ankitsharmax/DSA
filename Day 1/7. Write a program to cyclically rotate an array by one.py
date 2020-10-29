'''
Day 1:
    - 7. Write a program to cyclically rotate an array by one.

'''

print("Enter the values for the array: ")
array = list(map(int, input().split()))

print("\nArray after rotating the array cyclically")
temp = ['None']*len(array)
temp[0] = array[-1]
for i in range(len(array)-1):
    temp[i+1] = array[i]

print(temp)
