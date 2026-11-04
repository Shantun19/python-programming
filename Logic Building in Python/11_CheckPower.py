def isPower(x , y):
    """
    if x = 1 then whatever the power of x is we get always 1 so only we can return true when y is also 1 
    because 1 to the power any positive number not give bigger positive no. then 1
    """
    if x == 1:
        return y == 1
    if y == 1:
        return True
    power = 1
    while power < y:
        power = power * x
    return power == y

def isPowerUsingExponentiationBinarySearch(x , y):
    if y == 1:
        return True
    if x == 1:
        return y == 1

    power = x
    higher = 1
    
    while power < y:
        power = power * power
        higher = higher*2
    
    # using the binary searcg technique
    lower = 0

    while lower <= higher:
        mid = (lower + higher)//2
        result = x ** mid
        if result == y:
            return True
        elif result < y:
            lower + mid + 1
        else:
            high = mid - 1
    
    return False

if __name__ == "__main__":
    x = int(input("Enter first Number ! "))
    y = int(input("Enter second Number !"))

    print(isPower(x,y))

    # Better Approach – Exponentiation and Binary Search
    print(isPowerUsingExponentiationBinarySearch(x,y))
