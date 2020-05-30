from performance import performance


# Using Generator
@performance
def fib(number):
    first = 0
    second = 1
    for i in range(number):
        yield first
        third = second + first
        first = second
        second = third




# Using usual list approach
# @performance no point adding performance as it goes one by one.
def fib2(number):
    first = 0
    second = 1
    fibo = [0, 1]
    for i in range(2, number):
        third = second + first
        first = second
        second = third
        fibo.append(third)
    return fibo

print(fib(15))
