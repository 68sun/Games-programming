a = 4

def insideFunction():
    a = 17
    print("Value of a inside function:", a)
    
def insideFunctionGlobal():
    global a
    a = 17
    print("Value of a inside function:", a)

insideFunction()
print("Value of a outside function", a)

insideFunctionGlobal()
print("Value of a outside function", a)
