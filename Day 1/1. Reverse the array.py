'''
Day 1:
    -1. Reverse the array

'''

def reverse(arr):
    temp_arr = []
    print('Simple using list array')
    print(arr[::-1])

    print('using for loop')
    for i in range(len(arr)-1,-1,-1):
        temp_arr.append(arr[i])

    return temp_arr
        


print("Enter values for the array")
array = list(map(int,input().split()))

print(reverse(array))
