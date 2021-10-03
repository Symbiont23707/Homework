"""Use function from Task 5.5 for validating input, handle all exceptions
      and print user friendly output."""
from Task7_5 import number_checker, NumberLessThanTwo, IsNotEvenError

def IsNumberPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def Goldbach(number):
    """program for proving Goldbach's conjecture. Program accepts number for input and print result."""
    if number == 4:
        print("2 + 2")
    for i in range(3, number):
        if IsNumberPrime(i):
            for x in range(i, number):
                if IsNumberPrime(x) and number == i + x:
                    print(f"{i} + {x}")

    while True:
        """For pressing 'q' program succesfully close."""
        next_session = input("Do you want to continue?(continue(c)/quit(q): ")
        if next_session == 'q':
            return False

        else:
            number = int(input("Enter your number: "))
            try:
                number_checker(number)
            except TypeError:
                print("Number is not a int")
            except IsNotEvenError:
                print("Number is not a even")
            except NumberLessThanTwo:
                print("Number more than two")
            else:
                Goldbach(number)

def main():
    Goldbach(8)

if __name__ == "__main__":
    main()