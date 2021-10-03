from contextlib import contextmanager
"""context manager for opening and working with file, including handling exceptions with @contextmanager decorator"""
@contextmanager
def open_file(file_name, mode="r"):
    file = open(file_name, mode)
    try:
        yield file
    except FileNotFoundError as exc:
        print(exc)
    finally:
        file.close()

with open_file("test7_2.txt", "r") as f:
    print(f.readline())