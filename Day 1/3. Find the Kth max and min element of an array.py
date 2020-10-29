'''
Day 1:
    -3. Find the Kth max and min element of an array

    Task: Find the k-th smallest and largest element in a giver array
            Eg: Find 3rd smallest element in a given array
            Eg: Find 4th largest element in a given array

'''

def kth_min_max(arr, smallest, largest):
    arr1 = arr
    arr2 = arr
    temp_min = []
    temp_max = []
    for _ in range(smallest):
        temp_min.append(min(arr1))
        arr1.remove(min(arr1))

    for _ in range(largest):
        temp_max.append(max(arr2))
        arr2.remove(max(arr2))

    return temp_min[-1], temp_max[-1]

print('Enter the values for the array: ')
array = list(map(int,input().split()))

print('Enter the k-th smallest values to find: ')
smallest = int(input())

print('Enter the k-th largest values to find: ')
largest = int(input())

minArr, maxArr = kth_min_max(array, smallest, largest)
print('k-th smallest value in the array: ',str(minArr))
print('k-th largest value in the array: ',str(maxArr))
