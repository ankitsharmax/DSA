'''
print(*array): This will print the list/array without the brackets
                One of the most useful technique that will help to not use
                for loop to print each charachter line by line  :)
'''


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ls = [0 for i in range(arr.count(0))] + [1 for i in range(arr.count(1))] + [2 for i in range(arr.count(2))]
    print(*ls)
