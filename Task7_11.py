def endless_fib_generator():
    """generator which will geterate Fibonacci numbers endlessly"""
    Fn_2 = 1
    Fn_1 = 0

    while True:
        yield Fn_1 + Fn_2
        Fn_2, Fn_1 = Fn_1, Fn_2 + Fn_1

def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen), end=" ")


if __name__ == "__main__":
    main()
