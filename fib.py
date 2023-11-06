def fib_iterative(n):
    a = 0
    b = 1
    for _ in range(2, n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


fib_iterative(10)


def fibonacci(num):
    if num == 0:
        return 0    
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = 10
# print(fibonacci(n))
fib_series = []

for i in range(n):
    fib_series.append(fibonacci(i))

print(fib_series)
