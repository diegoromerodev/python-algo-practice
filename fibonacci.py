def fibonacci(nth):
    if nth == 1 or nth == 2: return 1
    return fibonacci(nth - 1) + fibonacci(nth - 2)

print(fibonacci(10))