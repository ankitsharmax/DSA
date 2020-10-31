'''
kth smallest element in the array
iterate from last to find the kth largest element in the array

'''


t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    k = int(input())
    array.sort()
    print(array[k-1])
    
