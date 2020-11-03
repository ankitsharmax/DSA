T = int(input())
for _ in range(T):
    str1 = input()

    cnt = 0
    count0 = 0
    count1 = 0

    for i in range(len(str1)):
        if str1[i] == '0':
            count0 += 1
        elif str1[i] == '1':
            count1 += 1

        if count0 == count1:
            cnt += 1

    print(cnt)
