# the time complexity of this code would be O(N)
def checkForPrime(num):
    i = 2
    for i in range(2 , num):
        if num%i == 0:
            return False
    return True

# check a number is prime or not using the square root trial division method.
def checkIsPrimeUsingSquareRootTrialDivisionMethod(num):
    if num <= 2:
        return False
    i = 2
    while i*i <= num:
        if num%i == 0:
            return False
        i = i+1
    return True

if __name__ == "__main__":
    num = int(input("Enter any Integer value "))
    # change the function name to execute the specific function
    if checkIsPrimeUsingSquareRootTrialDivisionMethod(num):
        print(f'{num} is a prime number !')
    else:
        print(f'{num} is not a prime number !')