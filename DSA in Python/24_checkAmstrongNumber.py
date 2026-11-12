def getDigits(num):
    count = 0
    while num != 0:
        count = count + 1
        num = num // 10
    return count

def findSum(num , power):
    result = 1
    for i in range(1 , power+1):
        result = result * num
    return result

def isAmstrongNumber(num):
    # first count the digits of a given number
    temp = num
    totalDigits = getDigits(num)
    totalSum = 0
    while temp != 0:
        # get the last digit of the number
        lastDigit = temp % 10
        totalSum = totalSum + findSum(lastDigit , totalDigits)
        temp = temp // 10
    return num == totalSum

def isAmstrongNumberUsingString(num):
    # convert the number into the string
    numberString = str(num)
    # get the length of the string as a digits
    digits = len(numberString)
    result = 0
    for i in numberString:
        # convert the number into the string and use the exponent operation
        result = result + int(i)**digits
    return result == num

if __name__ == "__main__":
    num = int(input("Enter any Integer value "))
    if isAmstrongNumber(num):
        print(f'{num} is a amstrong number !')
    else:
        print(f'{num} is not a amstrong number !')

    if isAmstrongNumberUsingString(num):
        print(f'{num} is a amstrong number !')
    else:
        print(f'{num} is not a amstrong number !')