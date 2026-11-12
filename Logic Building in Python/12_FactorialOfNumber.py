def findFactorial(num):
    fact = 1
    for i in range(1 , num+1):
        fact = fact * i
    return fact

def findFactorialUsingRecursion(num):
    if num == 1:
        return 1
    return num * findFactorialUsingRecursion(num - 1)

if __name__ == "__main__":
    num = int(input("Enter any Integer value ! "))
    print(f'the factorial of {num} is :' , findFactorial(num))

    # find factorial using the recursive approach
    print(f'the factorial of {num} using the recursion is : ' , findFactorialUsingRecursion(num))