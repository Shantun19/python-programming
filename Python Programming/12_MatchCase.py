x = 4

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3:
        print("x is three")
    case 4:
        if x%2 == 0:
            print(f"{x} is an even number with value {x}")
    # for the default case we use underscore(_)
    case _:
        print("default case is run")