def find_root():
    while True:
        try :
            x_str = input("enter number to find the root of ")#gets numberb from user
            x = float(x_str)
            break
        except ValueError:
            print("invalid input")
    while True:
        try:
            power_str = input("enter nth root ")#gets nth root from user
            power = float(power_str)
            break   
        except ValueError:
            print("invalid input")

    epsilon = 0.01#sets accuracy

    if x == 0:
       print(f"the {power}-nth power of 0 is 0")
       return 0
    elif x < 0 and power % 2 == 0:#handles cases of negative numbers with even powers
        print(f"a negative number has no real even-powered ({power} root)")
        return None 
    else :
        low = min(0,x)
        high = max(1,x)
        ans = (low + high)/2.0

        while abs(ans**power - x) >= epsilon:#user bisection search to find root 
            if ans**power < x:
                low = ans
            else:
                high = ans
            ans = (low + high)/2.0

        print(f"the approximate {power}-th  root of {x} is : {ans}")
        return ans    