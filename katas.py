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
    if n < 0:
        print("Cannot compute a negative number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
