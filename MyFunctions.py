def mySum(x: float, y: float):
    return x + y

def myDiv(x: float, y: float):
    if y == 0:
        raise ValueError("Not 0 allowed for y")
    return x / y