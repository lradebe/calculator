def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return b * 2

def division(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b