#Create a function called factorial() that returns the factorial of a given variable x.
def factorial(x):

    y = 1

    for i in range (1, x + 1):
        y = y*i
    return y

print(factorial(5))