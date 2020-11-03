from itertools import permutations

T = int(input())
for _ in range(T):
    s = input()
    perm = permutations(s)
    temp = []
    for e in perm:
        temp.append(''.join(e))
    temp.sort()
    print(*temp)
