'''
Day 1:
    - 8. Find Largest sum contiguous Subarray [V. IMP]
    To solve this we'll use kadane's algorithm


'''
from sys import maxsize #to get maximum size possible

def subarray_sum(arr):
    max_so_far = -maxsize
    max_end_here = 0

    for i in range(len(arr)):
        max_end_here = max_end_here + arr[i]
        if max_so_far < max_end_here:
            max_so_far = max_end_here

        if max_end_here < 0:
            max_end_here = 0

    return max_so_far


print('Enter the values for the array: ')
array = list(map(int,input().split()))
print('\nOur array is: ')
print(array)

print('\nLargest sum of contiguous subarray:')
print(subarray_sum(array))
