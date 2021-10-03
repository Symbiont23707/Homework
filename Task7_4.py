def supressing_exceptions(func):
    """Implement decorator for supressing exceptions. If exception not occure write log to console."""
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("We have a problem")

    return wrapper


@supressing_exceptions
def divide(x, y):
    print(x / y)


def main():
    divide(5, 0)


if __name__ == "__main__":
    main()
