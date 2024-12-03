def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a*b
    return result

def divide(a, b):
    if b != 0:
        result = a/b
        return result
    else:
        print('ERROR: CAN\'T DIVIDE BY 0')
        return None