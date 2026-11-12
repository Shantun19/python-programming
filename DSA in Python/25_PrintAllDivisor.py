def printAllDivisor(num):
    divisors = []
    for i in range(1 , num+1):
        if num%i == 0:
            divisors.append(i)
    print(divisors)

def printAllDivisorApproach2(num):
    divisors = []
    i = 1
    while i*i <= num:
        if num%i == 0:
            divisors.append(i)
            if i != num//i:
                divisors.append(num//i)
        i = i + 1
    print(divisors)

if __name__ == "__main__":
    num = int(input("Enter any integer value "))
    # print all the divisor using the iterative approach
    printAllDivisor(num)
    # print all the divisor using the better approach
    printAllDivisorApproach2(num)