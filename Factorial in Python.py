
#Function that return the factorial of a number
def factorial(num):
    if type(num) is not int:
        print("Not an integer, please enter an integer.")
        return None
    elif num < 0:
        print("Negative number, please enter a positive number.")
        return None
    elif num == 0:
        return 1
    else:
        fac=1
        for i in range(1,num+1):
            fac=fac*i
        return fac
    

print(factorial(5))        
