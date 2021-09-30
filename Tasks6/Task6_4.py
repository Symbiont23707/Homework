class Bird:
    """class Bird with an attribute name and methods fly and walk."""
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("{} bird can walk".format(self.name))
    def fly(self):
        pass


class FlyingBird(Bird):
    """class FlyingBird with attributes name, ration"""
    def __init__(self, name):
        super().__init__(name)
        self.ration = "mostly grains"

    def eat(self):
        """Implemented the method eat"""
        print(f"It eats {self.ration}")

    def fly(self):
        print("{} bird can fly".format(self.name))

    def __str__(self):
        return f"{self.name} can walk and fly"

class NonFlyingBird(FlyingBird):
    """class NonFlyingBird with same characteristics but which obviously without attribute fly"""
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = f"mostly {ration}"

    def eat(self):
        print(f"It eats {self.ration}")

    def walk(self):
        print(f"{self.name} bird can walk")

    def swim(self):
        print(f"{self.name} bird can swim")

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def __str__(self):
        return f"{self.name} can walk and swim"

class SuperBird(NonFlyingBird, FlyingBird):
    """class SuperBird which can do all of it: walk, fly, swim and eat"""
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats {self.ration}")

    def walk(self):
        super().walk()

    def swim(self):
        super().swim()

    def fly(self):
        super(FlyingBird).fly()

    def __str__(self):
        return f"{self.name} can walk, swim and fly"

b = Bird("Any")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
#p.fly()
p.eat()

c = FlyingBird("Canary")
print(str(c))
c.eat()

s = SuperBird("Gull")
print(str(s))

s.eat()
