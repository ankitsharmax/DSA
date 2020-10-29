'''
Day 1:
    -2. Find the maximum and minimum element in an array

'''

def min_max(arr):
    print('Using python methods')
    print('Minimum element: ',str(min(arr)))
    print('Maximum element: ',str(max(arr)))
    
    print('\nUsing for loops')
    minArr = maxArr = arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] < minArr:
            minArr = arr[i+1]
        if arr[i+1] > maxArr:
            maxArr = arr[i+1]
    return minArr, maxArr		


print("Enter values for the array")
array = list(map(int,input().split()))

minArr, maxArr = min_max(array)
print('Minimum element in the array is: ',str(minArr))
print('Maximum element in the array is: ',str(maxArr))
