def factorial(p):
    m = 1
    if p==1:
        return p
    elif p==0:

        print("factorial of 0 is 1")
    else:
        m = p*factorial(p-1)
    return m
print(factorial(5))
