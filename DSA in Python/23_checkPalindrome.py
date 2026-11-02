def reversedTheNumber(num):
    reversedNumber = 0

    while num != 0:
        reversedNumber = (reversedNumber * 10) + (num % 10)
        num = num // 10

    return reversedNumber


def checkPalindrome(num):
    return num == reversedTheNumber(num)


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if checkPalindrome(num):
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")
