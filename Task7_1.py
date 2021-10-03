class context_manager:
    """class-based context manager for opening and working with file"""
    def __init__(self, file_name, mode="r"):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        else:
            print(f"{exc_type}, {exc_val}, {exc_tb}")

with context_manager("test7_1.txt") as file:
    print(file.read())