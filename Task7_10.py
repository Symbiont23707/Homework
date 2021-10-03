def endless_generator():
    """generator which will generate odd numbers endlessly"""
    start = 1
    while True:
        yield start
        start += 2

def main():
   func = endless_generator()
   while True:
       print(next(func))

if __name__ == "__main__":
    main()