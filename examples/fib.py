

# Naive recursion
def fib_rec(num):
    if num <= 0:
        return 0

    if num <= 2:
        return 1

    return fib_rec(num-2) + fib_rec(num-1)


def fib_loop(num):
    if num <= 0:
        return 0

    if num <= 2:
        return 1

    current = 2
    current_minus_1 = 1

    for i in range(3, num):
        current_minus_2 = current_minus_1
        current_minus_1 = current
        current = current_minus_2 + current_minus_1

    return current


def tester(fib_func: callable):
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    result = {
        10: 55,
        20: 6765,
        50: 12586269025,
        100: 354224848179261915075
    }
    for i in range(10):
        assert fib_func(i) == expected[i]

    for key in result.keys():
        assert fib_func(key) == result[key]

    print("pass")





