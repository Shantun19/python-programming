def getGCD(num1 , num2):
    # base condition
    if num1 == 0 or num2 == 0:
        return max(num1 , num2)
    # first get the minimun from both the number because gcd <= min(a,b) we no need to check for the values which is greater than a.
    min_number = min(num1 , num2)
    # we need to find the greater divisor so we will starts the loop from the end means in the reverse order.
    for i in range(min_number , 2 , -1):
        if num1%i == 0 and num2%i == 0:
            return i

def getGCDUsingEuclidean(num1 , num2):
    # base condition
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 > num2:
        return getGCDUsingEuclidean(num1 - num2 , num2)
    return getGCDUsingEuclidean(num1 , num2 - num1)

def getGCDUsingEuclideanUsingDivisibility(num1 , num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 > num2:
        if num1%num2 == 0:
            return num2
        return getGCDUsingEuclideanUsingDivisibility(num1-num2 , num2)
    if num2%num1 == 0:
        return num1
    return getGCDUsingEuclideanUsingDivisibility(num1 , num2-num1)

def getGCDUsingEuclideanUsingCheckingRemainder(num1 , num2):
    return a if b == 0 else getGCDUsingEuclideanUsingCheckingRemainder(num2 , num1%num2)

if __name__ == "__main__":
    num1 = int(input("Enter the first Number ! "))
    num2 = int(input("Enter the second Number ! "))

    # find gcd of 2 number using the iterative approach
    print("the gcd of {num1} and {num2} is " , getGCD(num1 , num2))

    # find gcd of 2 number using the euclidean algorithms
    # Note: This approach may cause a stack overflow for large inputs due to excessive recursive calls.
    print("the gcd of {num1} and {num2} using the euclidean algorithm is " , getGCDUsingEuclidean(num1 , num2))

    #  Euclidean Algorithm using Subtraction by Checking Divisibility - O(min(a, b)) Time and O(min(a, b)) Space
    # Note: This approach may cause a stack overflow for large inputs due to excessive recursive calls.
    print("the gcd of {num1} and {num2} using the euclidean algorithm by checking the divisibility" , getGCDUsingEuclideanUsingDivisibility(num1 , num2))

    # Optimized Euclidean Algorithm by Checking Remainder
    print("the gcd of {num1} and {num2} using the euclidean algorithm by checking the Remainder" , getGCDUsingEuclideanUsingCheckingRemainder(num1 , num2))
