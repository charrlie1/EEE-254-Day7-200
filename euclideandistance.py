def euclidean_distance():
    try:
        x1 = float(input("enter x-coordinate for the intial position:"))
        y1 = float(input("enter y-coordinate for the intial position:"))
        x2 = float(input("enter x-coordinate for the final position:"))
        y2 = float(input("enter y-coordinate for the final position:")) #gets input from user
        t = (x2 - x1)**2 + (y2 - y1)**2
        return t 
#returns the calcuateed  value of t based on the user input
    except ValueError:
        print("invaid input")
        return None
    
def edistance(n,epsilon):
    if n is None:
        return None
    if n < 0:
        raise ValueError("cannot find a negative square root")
    if n == 0:
        return 0.0    


    low = 0.0

    high = max(1, n)

    while high - low > epsilon:
        ans = (high + low)/2.0
        if ans**2 > n:
            high = ans
        else:
            low = ans
    return (high + low)/2.0 #uses bisection search to get square root 
t_value = euclidean_distance() #gets the calculated value of t

if t_value is not None:
    sqrt_precision=0.01 #sets the accuracy for the square root
    distance_approx =edistance(t_value, sqrt_precision)

    if distance_approx is not None:
        print(f"the approximate  euclidean distance is{distance_approx}")
45