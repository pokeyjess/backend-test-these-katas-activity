def add(x, y):
    return x + y


def multiply(x, y):
    result = 0

    for _ in range(abs(y)):
        result = add(result, x)

    return -result if y < 0 else result


def power(x, n):
    result = 1

    for _ in range(n):
        result = multiply(result, x)

    return result


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = multiply(result, i)
    if n < 0:
        print("Cannot compute a negative number")
    else:
        return result


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    if n < 0:
        print("Cannot compute a negative number")
    else:
        return a
