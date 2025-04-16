def Ackermann_function(m,n):
    if not isinstance(m,int) or m < 0:
        raise ValueError("m must be a positve integer ")
    if not isinstance(n,int) or n < 0:
        raise ValueError("n must be a positve integer")
    
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann_function(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann_function(m - 1, Ackermann_function(m , n - 1))
try :
    m_val = int(input("enter non negative value for m :"))
    n_val = int(input("enter non negative value for n :"))

    result = Ackermann_function(m_val,n_val)
    print(f"A({m_val,n_val}) = {result}")
except ValueError as e:
    print(f"Error : {e}")
except Exception as e:
    print(f"an unexpected error as : {e}")
