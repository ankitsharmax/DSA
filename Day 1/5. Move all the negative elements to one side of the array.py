'''
Day 1:
    - 5. Move all the negative elements to one side of the array 

    Input:  -12, 11, -13, -5, 6, -7, 5, -3, -6
    Output: -12, -13, -5, -7, -3, -6, 5, 6, 11
    
'''

def rearrange(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr

print('Enter the values for the array')
array = list(map(int,input().split()))
print('array before arranging')
print(array)

print('\nArray after rearranging')
print(rearrange(array))
