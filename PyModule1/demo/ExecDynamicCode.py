def exec_code(n: int):
    dynamicCode = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(""" + str(n) + """)) 
"""
    print(dynamicCode)
    exec(dynamicCode)


if __name__ == '__main__':
    exec_code(5)
