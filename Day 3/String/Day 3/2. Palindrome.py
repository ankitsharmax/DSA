T = int(input())
for _ in range(T):
    text = input()
    if text == text[::-1]:
        print(text + " is palindrome")
    else:
        print(text + " is not palindrome")
