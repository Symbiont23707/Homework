import time
from contextlib import ContextDecorator

class context_manager_with_execution_time(ContextDecorator):
    """Implement decorator with context manager support for writing execution time to log-file. See contextlib module."""

    def __init__(self, file_name: str, mode="a"):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        f = open(self.file_name, self.mode)
        f.write(f"{time.perf_counter() - self.start_time:.4f} sec \n")
        f.close()

@context_manager_with_execution_time("test7_3.txt")
def func():
    print("Let's gooo")

def main():
    func()

if __name__ == "__main__":
    main()