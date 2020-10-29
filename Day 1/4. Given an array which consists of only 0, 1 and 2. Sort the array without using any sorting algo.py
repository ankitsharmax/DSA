'''
Day 1:
    - 4. Given an array which consists of only 0, 1 and 2.
         Sort the array without using any sorting algo.

'''

print("Enter the values for the array: ")
array = list(map(int,input().split()))

print("Array Before sorting")
print(array)
print("\nArray after sorting")
print(sorted(array))
