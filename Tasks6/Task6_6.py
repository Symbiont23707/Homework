class Singleton:
    """A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance"""
    instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = super(Singleton, cls).__new__()
        return cls.instance

class Sun:
    @staticmethod
    def inst():
        return Singleton

p = Sun.inst()
f = Sun.inst()
print(p is f)