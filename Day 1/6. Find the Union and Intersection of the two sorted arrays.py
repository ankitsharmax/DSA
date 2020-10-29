'''
Day 1:
    - 6. Find the Union and Intersection of the two sorted arrays.


'''
def union(array1, array2):
    temp = []
    for e in array1:
        if e not in temp:
            temp.append(e)
    for e in array2:
        if e not in temp:
            temp.append(e)

    return temp

def intersection(array1, array2):
    temp = []
    for e in array2:
        if e in array1:
            temp.append(e)
    return temp


print('Enter the values for the first array: ')
array1 = list(map(int,input().split()))

print('\nEnter the values for the second array: ')
array2 = list(map(int,input().split()))

print("\nUnion of two arrays")
print(union(array1, array2))
print("\nIntersection of two arrays")
print(intersection(array1, array2))
