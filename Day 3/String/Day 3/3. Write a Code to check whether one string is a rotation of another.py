'''
Day 3:
    - 3. Write a Code to check whether one string is a rotation of another

    Algorothm:
    1. Concatinate string1 with string1 to temp
    2. if string2 is a subset of temp then
            string2 is a rotation of string1

'''
T = int(input())
for _ in range(T):
    string1 = input()
    string2 = input()

    if len(string1) != len(string2):
        print('Invalid Input')

    temp = string1 + string1
    if temp.count(string2)<1:
        print(f'String 2 "{string2}" is not a rotation of string 1 "{string1}"')
    else:
        print(f'String 2 "{string2}" is a rotation of string 1 "{string1}"')
